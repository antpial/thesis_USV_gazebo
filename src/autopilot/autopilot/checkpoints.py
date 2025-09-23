#!/usr/bin/env python3
#
# In this script boat sails on given azimuth
#

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import MagneticField
import math
from std_msgs.msg import Float64
from sensor_msgs.msg import NavSatFix
from dataclasses import dataclass

@dataclass
class GpsState:
    lat: float = 0.0
    lon: float = 0.0

class Checkpoints_node(Node):
    def __init__(self):
        super().__init__('Checkpoints_node')

        self.given_azimuth = 355.0
        self.given_position = GpsState(lat= -33.721365, lon=150.675268)
        self.v = 0.5
        self.d = 0.0
        self.left_thrust = 0.0
        self.right_thrust = 0.0

        self.current_azimuth = 0.0
        self.current_position = GpsState()    
        self.e = 0
        self.p = 0.05 # parametr regulatora P
        self.mag_x = 0.0 
        self.mag_y = 0.0
        self.mag_z = 0.0 

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
            '/gps',
            self.gps_callback,
            10
        )
        self.get_logger().info("Gps subscriber started!")

        # publishery na silniki
        self.left_pub = self.create_publisher(Float64, '/left_thrust', 10)
        self.right_pub = self.create_publisher(Float64, '/right_thrust', 10)


        # timer gdzie sie dzieje cala magia
        self.timer = self.create_timer(0.1, self.control_loop)


    def mag_callback(self, msg: MagneticField):

        self.mag_x = msg.magnetic_field.x
        self.mag_y = msg.magnetic_field.y
        self.mag_z = msg.magnetic_field.z

        azimuth_rad = math.atan2(self.mag_x, self.mag_y)
        self.current_azimuth = math.degrees(azimuth_rad)
        # Normalizacja do 0-360°
        if self.current_azimuth < 0:
            self.current_azimuth += 360.0


    def gps_callback(self, msg: NavSatFix):
        self.current_position.lat = msg.latitude
        self.current_position.lon = msg.longitude



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

    def calculate_azimuth(self):
        # zamiana stopni na radiany
        phi1 = math.radians(self.current_position.lat)
        phi2 = math.radians(self.given_position.lat)
        d_lambda = math.radians(self.given_position.lon - self.current_position.lon)

        x = math.sin(d_lambda) * math.cos(phi2)
        y = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(d_lambda)

        theta = math.atan2(x, y)
        bearing = (math.degrees(theta) + 360.0) % 360.0
        return bearing




    def control_loop(self):

        # kalkuluje azymut
        self.given_azimuth = self.calculate_azimuth()

        # licze blad normalizujac bo w stopniach jest modulo 360
        self.e = (self.given_azimuth - self.current_azimuth + 180.0) % 360.0 - 180.0

        # steruje wartoscia d (skret) regulatorem P
        self.d = self.e * self.p

        # ustawiam ciag na silnikach
        self.publish_thrust()
        

        # Logowanie lub publikacja
        self.get_logger().info("-------------------------------------------------------")
        self.get_logger().info(f"Given: {self.given_azimuth:.2f}°, Azymut: {self.current_azimuth:.2f}°, e = {self.e:.2f}°")
        self.get_logger().info(f"d: {self.d:.2f}%, v: {self.v}%, T_L: {self.left_thrust:.2f}%, T_R: {self.right_thrust:.2f}%")
        self.get_logger().info(f"curr. lat.: {self.current_position.lat:.6f}, curr. lon.: {self.current_position.lon:.6f}" )




def main(args=None):
    rclpy.init(args=args)
    node = Checkpoints_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
