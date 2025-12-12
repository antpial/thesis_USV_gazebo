#!/usr/bin/env python3
#
# In this script boat sails to given checkpoints while using ekf from robot_localization
#

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import MagneticField
import math
from std_msgs.msg import Float64
from sensor_msgs.msg import NavSatFix
from dataclasses import dataclass
from collections import deque
import math
import copy
import xml.etree.ElementTree as ET
from msg_interfaces.msg import InternalState
from sensor_msgs.msg import Imu


@dataclass
class GpsState:
    lat: float = 0.0
    lon: float = 0.0

@dataclass
class MagState:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0



class Los_node(Node):
    def __init__(self):
        super().__init__('Los_node')

        self.LOS_ON = True

        # Parametry ruchu
        self.v = 0.6    # predkosc
        self.given_position = GpsState(lat= -33.721365, lon=150.675268)  # punkt docelowy
        self.starting_position = GpsState(lat=0, lon=0) # pozycja startowa (do liczenia dryfu)
        self.Kp_az = 0.025 # .025 to optymalna wyliczona wartosc dla los
        self.Kd_az = 0.5 # wzmocnienie czlonu D regulatora obrotu
        self.yaw_vel = 0.0 # predkosc katowa yaw z imu

        # Dane pomiarowe
        self.current_position = GpsState()
        self.mag_vector = MagState()

        # Sterowanie
        self.d = 0.0    # skret (-1 do 1)
        self.e = 0.0    # blad (potrzebny azymut - aktualny azymut)
        self.left_thrust = 0.0  # moc lewego silnika [-1,1]
        self.right_thrust = 0.0 # moc prawego silnika [-1,1]

        # Azymuty
        self.given_azimuth = 0.0    # azymut do punktu docelowego
        self.current_azimuth = 0.0  # aktualny azymut
        self.distance = 0.0 # odleglosc do punktu docelowego
        self.magnetic_declination = -12.82 # deklinacja magnetyczna w stopniach

        # LOS
        self.P_los = 0.0 # skladnik proporcjonalny regulatora P dla LOS
        self.de = 0.0 # odleglosc od linii prostej wyznaczonej przez punkty startowy i docelowy
        self.Kp_los = 9.0 # wspolczynnik wzmocnienia regulatora P dla LOS
        self.Ki_los = 0.856 # wspolczynnik wzmocnienia regulatora I dla LOS
        self.Kd_los = 30.0 # wspolczynnik wzmocnienia regulatora D dla LOS
        # self.Kp_los = 0.0 # wspolczynnik wzmocnienia regulatora P dla LOS
        # self.Ki_los = 0.0 # wspolczynnik wzmocnienia regulatora I dla LOS
        # self.Kd_los = 0.0 # wspolczynnik wzmocnienia regulatora D dla LOS
        self.I_los = 0.0 # skladnik calkujacy regulatora I dla LOS
        self.D_los = 0.0 # skladnik rozniczkujacy regulatora D dla LOS
        self.error_history = deque(maxlen=600)  # przechowuje ostatnie 3 min błędów do całkowania
        self.windup_limit = 44.0  # limit anty-windup dla całki
        self.timer_period = 0.1  # sekundy
        self.last_de = 0.0  # ostatnia wartość de do obliczania D
        # self.timer = self.create_timer(self.timer_period, self.calculate_I)

        #Prawdziwy LOS
        self.Delta = 12.25
        self.sigma = 0.85

        #checkpoints
        self.checkpoints = [] # lista wszystkich punktów docelowych (name, lat, lon, alt)
        self.current_checkpoint_index = 0 # indeks aktualnego punktu docelowego
        self.distance_threshold = 5.0 # odleglosc w metrach do punktu docelowego przy ktorej uznajemy ze dotarlismy do punktu
        self.reached_all_checkpoints = False # flaga czy dotarlismy do wszystkich punktow

        # czettoliwosci pida kaskadowego
        self.freq_outer = 5.0   # 2 Hz dla GPS/Nawigacji (Pętla zewnętrzna)
        self.freq_inner = 20.0  # 20 Hz dla Silników/IMU (Pętla wewnętrzna)
        
        self.dt_outer = 1.0 / self.freq_outer
        self.dt_inner = 1.0 / self.freq_inner

        # --- TIMERY ---
        # 1. Pętla Wewnętrzna (Szybka) - Sterowanie silnikami i kursem
        self.timer_inner = self.create_timer(self.dt_inner, self.inner_loop_control)
        
        # 2. Pętla Zewnętrzna (Wolna) - Nawigacja, LOS, Checkpointy
        self.timer_outer = self.create_timer(self.dt_outer, self.outer_loop_navigation)
        # publisher stanu wewnetrznego
        self.timer = self.create_timer(self.timer_period, self.publish_internal_state)

        # Subskrybujem /magnetometer
        self.subscription = self.create_subscription(
            MagneticField,
            '/magnetometer',
            self.mag_callback,
            10
        )
        self.get_logger().info("Magnetometer subscriber started!")

        # Subskrybuje /gps
        self.subscription = self.create_subscription(
            NavSatFix,
            '/gps/perfect',
            self.gps_callback,
            10
        )
        self.get_logger().info("Gps subscriber started!")

        self.imu_sub = self.create_subscription(
            Imu,
            '/imu',  # Sprawdź nazwę tematu!
            self.imu_callback,
            10
        )
        self.get_logger().info("IMU subscriber started!")

        # publishery na silniki
        self.left_pub = self.create_publisher(Float64, '/left_thrust', 10)
        self.right_pub = self.create_publisher(Float64, '/right_thrust', 10)

        # Wczytuje punkty docelowe z pliku checkpoints_list.kml
        self.get_checkpoints()

        # timer gdzie sie dzieje cala magia
        # self.timer = self.create_timer(0.1, self.control_loop)

        # publisher stanu wewnetrznego
        self.diag_pub = self.create_publisher(InternalState, '/usv/stan', 10)


    def outer_loop_navigation(self):
       
        # jeśli dotarlismy do wszystkich punktow to nic nie robimy
        if self.reached_all_checkpoints:
            return
        
        # kalkuluje odleglosc od wyznaczonej prostej
        self.last_de = copy.deepcopy(self.de)
        self.de = self.get_drift()
       

        if(not self.LOS_ON):
            # Kalkuluje skladnik calkujacy I dla LOS
            self.calculate_I()
            self.calculate_D_los()
            # kalkuluje docelowy azymut
            self.given_azimuth = self.calculate_new_azimuth() + self.calculate_P_los() + self.I_los + self.D_los # korekta azymutu docelowego o odleglosc od linii prostej
            if self.given_azimuth < 0:
                self.given_azimuth += 360.0
            if self.given_azimuth >= 360.0:
                self.given_azimuth -= 360.0

        if(self.LOS_ON):
            self.calculate_I_rLOS()
            # Najpierw obliczamy kąt samej ścieżki (niezależnie od pozycji robota)
            path_angle_rad = math.radians(self.calculate_path_angle())
            # Obliczamy korektę ILOS (w radianach!)
            # Uwaga na znaki: w Twoim get_drift musisz sprawdzić, czy błąd jest dodatni 
            # gdy jesteś z lewej czy prawej strony. 
            # Zakładając standard: +de oznacza bycie z prawej strony trasy -> musimy skręcić w lewo (-).
            correction_angle = math.atan((self.de + self.sigma * self.I_los) / self.Delta)
            
            # Wynikowy kąt w radianach
            target_yaw_rad = path_angle_rad + correction_angle # Minus, aby kontrować błąd
            
            # Konwersja na stopnie i normalizacja 0-360
            self.given_azimuth = math.degrees(target_yaw_rad)
            self.given_azimuth = (self.given_azimuth + 360) % 360


        # kalkuluje odleglosc do punktu docelowego
        self.distance = self.get_distance_from_lat_lon_in_km()

        # sprawdzam czy dotarlismy do punktu docelowego
        if self.distance < self.distance_threshold:
            self.reached_checkpoint()

        # wyswietlam logi
        self.show_logs()


    def inner_loop_control(self):
        
        if self.reached_all_checkpoints:
            self.left_thrust = 0.0
            self.right_thrust = 0.0
            self.publish_thrust()
            return
        
        # kalkuluje odleglosc do punktu docelowego
        self.distance = self.get_distance_from_lat_lon_in_km()

        # kalkuluje aktualny azymut
        self.current_azimuth = self.calculate_current_azimuth()

        # licze blad azymutow normalizujac bo w stopniach jest modulo 360
        self.e = (self.given_azimuth - self.current_azimuth + 180.0) % 360.0 - 180.0

        # steruje wartoscia d (skret) regulatorem PD
        self.d = (self.e * self.Kp_az) + (self.yaw_vel * self.Kd_az) # dodaje skladnik z predkosci katowej yaw z imu

        # ustawiam ciag na silnikach
        self.publish_thrust()

    def calculate_D_los(self):
        # Oblicza składnik różniczkujący D dla regulatora LOS
        de_difference = self.de - self.last_de
        self.D_los = self.Kd_los * (de_difference / self.dt_outer)


    def imu_callback(self, msg: Imu):
        self.yaw_vel = msg.angular_velocity.z


    # Callbacki do subskrybcji
    def publish_internal_state(self):
        msg = InternalState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.id = 0
        # --- Sterowanie ---
        msg.v = float(self.v)
        msg.d = float(self.d)
        # --- Błędy sterowania ---
        msg.e = float(self.e)
        msg.de = float(self.de)
        # --- Nawigacja GPS ---
        msg.given_position_lat = float(self.given_position.lat)
        msg.given_position_lon = float(self.given_position.lon)
        msg.starting_position_lat = float(self.starting_position.lat)
        msg.starting_position_lon = float(self.starting_position.lon)
        # --- Wyjścia silników ---
        msg.left_thrust = float(self.left_thrust)
        msg.right_thrust = float(self.right_thrust)
        # --- Stan ---
        msg.given_azimuth = float(self.given_azimuth)
        msg.current_azimuth = float(self.current_azimuth)
        msg.distance = float(self.distance)
        # --- Diagnostyka PID/LOS ---
        msg.p_los = float(self.P_los)
        msg.i_los = float(self.I_los)
        msg.kp_los = float(self.Kp_los)
        msg.ki_los = float(self.Ki_los)
        msg.yaw_vel = float(self.yaw_vel)

        self.diag_pub.publish(msg)


    def mag_callback(self, msg: MagneticField):

        self.mag_vector.x = msg.magnetic_field.x
        self.mag_vector.y = msg.magnetic_field.y
        self.mag_vector.z = msg.magnetic_field.z


    def gps_callback(self, msg: NavSatFix):

        # aktualizuje aktualna pozycje
        self.current_position.lat = msg.latitude
        self.current_position.lon = msg.longitude

        if self.starting_position.lat == 0 and self.starting_position.lon == 0:
            self.starting_position.lat = msg.latitude
            self.starting_position.lon = msg.longitude
            self.get_logger().info(f"Ustawiono pozycje startowa: lat: {self.starting_position.lat}, lon: {self.starting_position.lon}")


    def get_checkpoints(self):
        # Wczytuje punkty docelowe z pliku checkpoints_list.kml
        tree = ET.parse('src/autopilot/autopilot/checkpoints_list.kml')
        root = tree.getroot()

        # przestrzeń nazw KML
        ns = {'kml': 'http://www.opengis.net/kml/2.2'}

        # Znajduje wszystkie Placemark
        placemarks = root.findall('.//kml:Placemark', ns)

        if not placemarks:
            self.get_logger().error("Nie znaleziono żadnych punktów w pliku checkpoints_list.kml")
            return

        for i, placemark in enumerate(placemarks):
            name = placemark.find('kml:name', ns).text
            coordinates = placemark.find('.//kml:coordinates', ns).text.strip()
            lon, lat, *alt = map(float, coordinates.split(','))
            alt = alt[0] if alt else 0.0

            # Dodajemy do listy wszystkich checkpointów
            self.checkpoints.append((name, lat, lon, alt))

            # Pierwszy punkt ustawiamy jako given_position
            if i == 0:
                self.given_position.lat = lat
                self.given_position.lon = lon
                self.get_logger().info(f"Wczytano pierwszy punkt docelowy: {name} (lat: {lat}, lon: {lon})")

        self.get_logger().info(f"Wczytano wszystkie checkpointy: {len(self.checkpoints)} punktów.")



    def publish_thrust(self):

        # Normuje skret. Nie moze przekraczac [-1,1]
        if(self.d < -1):
            self.d = -1
        if(self.d > 1):
            self.d = 1

        # Kalkuluje skret d na moc na silniku
        if(self.d <= 0):
            self.left_thrust = self.v * (1 + 2 * self.d)
            self.right_thrust = self.v
        else:
            self.left_thrust = self.v
            self.right_thrust = self.v * (1 - 2 * self.d)

        msg_left = Float64()
        msg_right = Float64()
        msg_left.data = self.left_thrust
        msg_right.data = self.right_thrust


        msg_left.data = self.left_thrust
        msg_right.data = self.right_thrust

        self.left_pub.publish(msg_left)
        self.right_pub.publish(msg_right)

    def calculate_new_azimuth(self):
        # zamiana stopni na radiany
        phi1 = math.radians(self.current_position.lat)
        phi2 = math.radians(self.given_position.lat)
        d_lambda = math.radians(self.given_position.lon - self.current_position.lon)
        y = math.sin(d_lambda) * math.cos(phi2)
        x = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(d_lambda)
        theta = math.atan2(y, x)
        bearing = (math.degrees(theta) + 360) % 360
        return bearing  
    
    def calculate_path_angle(self):
        # To jest kąt stałej linii trasy (od Startu do Celu)
        # Używamy self.starting_position zamiast self.current_position
        
        phi1 = math.radians(self.starting_position.lat)
        phi2 = math.radians(self.given_position.lat)
        d_lambda = math.radians(self.given_position.lon - self.starting_position.lon)
        
        y = math.sin(d_lambda) * math.cos(phi2)
        x = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(d_lambda)
        
        theta = math.atan2(y, x)
        bearing = (math.degrees(theta) + 360) % 360
        return bearing
    

    def calculate_current_azimuth(self):
        # obliczam kat sredniego wektora pola magnetycznego
        theta_rad = math.atan2(self.mag_vector.y, self.mag_vector.x)

        # Konwertuje z rad na stopnie
        theta_deg = math.degrees(theta_rad)     

        # atan2 oblicza kat od osi x, a polnoc jest na osi y, wiec trzeba obrocic
        azimuth = theta_deg + 90.0 + self.magnetic_declination

        # atan 2 daje wartosc w przedziale (-pi,pi), a nie (0,2pi), a wiec dla
        # azymutu z przedzialu (180,360) musimy przekalkulowac
        if(azimuth < 0):
            azimuth += 360.0

        return azimuth
    


    def get_distance_from_lat_lon_in_km(self):

        lat1 = self.current_position.lat
        lon1 = self.current_position.lon
        lat2 = self.given_position.lat
        lon2 = self.given_position.lon

        R = 6378137.0 # Radius of the earth in meters
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = (math.sin(dLat / 2) ** 2 +
            math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
            math.sin(dLon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        return d 
    

    def show_logs(self):   

        # Logowanie lub publikacja co sekunde
        self.get_logger().info("-----------------------------")
        self.get_logger().info(f"Given: {self.given_azimuth:.2f}°, Azymut: {self.current_azimuth:.2f}°, e = {self.e:.2f}°")
        self.get_logger().info(f"d: {self.d:.2f}%, v: {self.v}%, T_L: {self.left_thrust:.2f}%, T_R: {self.right_thrust:.2f}%")
        self.get_logger().info(f"cur. lat.: {self.current_position.lat:.5f}, cur. lon.: {self.current_position.lon:.5f}")
        self.get_logger().info(f"goal lat.: {self.given_position.lat:.5f}, goal lon.: {self.given_position.lon:.5f}")
        self.get_logger().info(f"cur. check.: {self.current_checkpoint_index}, Distance to goal: {self.distance:.2f} m")
        self.get_logger().info(f"Drift (de): {self.de:.2f} m, P_los: {self.P_los:.2f}, I_los: {self.I_los:.2f}, D_los: {self.D_los:.2f}")
        self.get_logger().info(f"Kp_az: {self.Kp_az:.4f}, Kd_az: {self.Kd_az:.4f}, Yaw_vel: {self.yaw_vel:.4f}")


    def reached_checkpoint(self):
        if self.reached_all_checkpoints:
            return

        name, lat, lon, alt = self.checkpoints[self.current_checkpoint_index]
        self.get_logger().info(f"Dotarłem do punktu: {name} (lat: {lat}, lon: {lon})")

        # Przechodzimy do następnego punktu
        self.current_checkpoint_index += 1

        if self.current_checkpoint_index >= len(self.checkpoints):
            self.get_logger().info("Dotarłem do wszystkich punktów docelowych!")
            self.reached_all_checkpoints = True
            self.v = 0.0  # zatrzymujemy łódź
            self.publish_thrust()
            return

        # Ustawiamy nowy punkt docelowy
        self.starting_position.lat = self.given_position.lat # ustawiamy punkt startowy na poprzedni punkt docelowy
        self.starting_position.lon = self.given_position.lon
        self.error_history.clear()  # czyścimy historię błędów dla całki
        self.I_los = 0.0  # resetujemy składnik całkujący
        name, lat, lon, alt = self.checkpoints[self.current_checkpoint_index]
        self.given_position.lat = lat
        self.given_position.lon = lon
        self.get_logger().info(f"Nowy punkt docelowy: {name} (lat: {lat}, lon: {lon})")


    def get_drift(self):
        R = 6371000  # Promień Ziemi w metrach

        # 1. Konwersja na radiany (bez zmian)
        lat1 = math.radians(self.starting_position.lat)
        lon1 = math.radians(self.starting_position.lon)
        
        lat2 = math.radians(self.given_position.lat)
        lon2 = math.radians(self.given_position.lon)
        
        lat0 = math.radians(self.current_position.lat)
        lon0 = math.radians(self.current_position.lon)

        # 2. Skalowanie Longitudy (To jest kluczowe!)
        # Obliczamy współczynnik "zwężania się" Ziemi na danej szerokości.
        # Dla małych odległości wystarczy wziąć cosinus szerokości startowej.
        lon_scale = math.cos(lat1)

        # 3. Obliczenia różnic (Delt) od razu w metrach (Linearyzacja)
        # Y to różnica szerokości (Północ-Południe)
        # X to różnica długości (Wschód-Zachód) przeskalowana przez cosinus
        
        # Wektor AB (odcinek trasy)
        line_y = (lat2 - lat1) * R
        line_x = (lon2 - lon1) * R * lon_scale

        # Wektor AC (od startu do robota)
        point_y = (lat0 - lat1) * R
        point_x = (lon0 - lon1) * R * lon_scale

        # 4. Wzór na odległość punktu od prostej (Cross Product)
        # | line_x * point_y - line_y * point_x | / dlugosc_linii
        numerator = (line_x * point_y) - (line_y * point_x)
        denominator = math.sqrt(line_x**2 + line_y**2)

        # Zabezpieczenie przed dzieleniem przez zero (gdy punkt startu = punkt celu)
        if denominator == 0:
            return math.sqrt(point_x**2 + point_y**2)

        # Wynik:
        # Jeśli zostawisz 'abs', masz odległość (zawsze dodatnią).
        # Jeśli usuniesz 'abs', wynik będzie miał znak (+/-), co powie Ci, 
        # czy jesteś z LEWEJ czy z PRAWEJ strony trasy (ważne dla sterowania!).
        distance = numerator / denominator

        return distance # Wynik w metrach

    def calculate_I(self):
        self.error_history.append(self.de)
        I = sum(self.error_history) * self.dt_outer # mnożymy przez czas między iteracjami (0.1s)
        I = self.Ki_los * I
        I = max(min(I, self.windup_limit), -self.windup_limit)  # ograniczenie anty-windup
        self.I_los = I

    def calculate_P_los(self):
        self.P_los = self.Kp_los * self.de
        return self.P_los
    
    def calculate_I_rLOS(self):
        # Implementacja wzoru (4b) ze zdjęcia
        
        # Mianownik: (y + sigma * y_int)^2 + Delta^2
        # Pamiętaj: self.de to Twoje 'y' (błąd odległości)
        denominator = (self.de + self.sigma * self.I_los)**2 + self.Delta**2
        
        # Licznik: Delta * y
        numerator = self.Delta * self.de
        
        # Pochodna y_int (dot_y_int)
        y_int_dot = numerator / denominator
        
        # Całkowanie numeryczne (metoda Eulera): nowa_wartość = stara + pochodna * czas
        self.I_los = self.I_los + (y_int_dot * self.dt_outer)

        # Opcjonalnie: Nadal warto trzymać limit (anty-windup) dla bezpieczeństwa
        self.I_los = max(min(self.I_los, self.windup_limit), -self.windup_limit)


def main(args=None):
    rclpy.init(args=args)
    node = Los_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
