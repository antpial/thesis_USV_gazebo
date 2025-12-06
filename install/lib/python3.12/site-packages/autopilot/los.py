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

        # Parametry ruchu
        self.v = 0.6    # predkosc
        self.given_position = GpsState(lat= -33.721365, lon=150.675268)  # punkt docelowy
        self.starting_position = GpsState(lat=0, lon=0) # pozycja startowa (do liczenia dryfu)
        self.p = 0.02 # parametr regulatora P
        self.alpha_gps = 0.1 # wspolczynnik filtra dolnoprzepustowego dla azymutu docelowego

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
        self.de = 0.0 # odleglosc od linii prostej wyznaczonej przez punkty startowy i docelowy
        self.Kp_los = 8.0 # wspolczynnik wzmocnienia regulatora P dla LOS

        #checkpoints
        self.checkpoints = [] # lista wszystkich punktów docelowych (name, lat, lon, alt)
        self.current_checkpoint_index = 0 # indeks aktualnego punktu docelowego
        self.distance_threshold = 5.0 # odleglosc w metrach do punktu docelowego przy ktorej uznajemy ze dotarlismy do punktu
        self.reached_all_checkpoints = False # flaga czy dotarlismy do wszystkich punktow

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
            '/gps/filtered',
            self.gps_callback,
            10
        )
        self.get_logger().info("Gps subscriber started!")

        # publishery na silniki
        self.left_pub = self.create_publisher(Float64, '/left_thrust', 10)
        self.right_pub = self.create_publisher(Float64, '/right_thrust', 10)

        # Wczytuje punkty docelowe z pliku checkpoints_list.kml
        self.get_checkpoints()

        # timer gdzie sie dzieje cala magia
        self.timer = self.create_timer(0.1, self.control_loop)

    # Callbacki do subskrybcji

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
        self.get_logger().info(f"Drift (de): {self.de:.2f} m")


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


    def control_loop(self):

        # jeśli dotarlismy do wszystkich punktow to nic nie robimy
        if self.reached_all_checkpoints:
            return
        
        # kalkuluje odleglosc od wyznaczonej prostej
        self.de = self.get_drift()
        
        # kalkuluje aktualny azymut
        self.current_azimuth = self.calculate_current_azimuth()

        # kalkuluje docelowy azymut
        self.given_azimuth = self.calculate_new_azimuth() + (self.Kp_los * self.de) # korekta azymutu docelowego o odleglosc od linii prostej

        # kalkuluje odleglosc do punktu docelowego
        self.distance = self.get_distance_from_lat_lon_in_km()

        # licze blad azymutow normalizujac bo w stopniach jest modulo 360
        self.e = (self.given_azimuth - self.current_azimuth + 180.0) % 360.0 - 180.0

        # steruje wartoscia d (skret) regulatorem P
        self.d = self.e * self.p

        # ustawiam ciag na silnikach
        self.publish_thrust()

        # sprawdzam czy dotarlismy do punktu docelowego
        if self.distance < self.distance_threshold:
            self.reached_checkpoint()

        # wyswietlam logi
        self.show_logs()



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
