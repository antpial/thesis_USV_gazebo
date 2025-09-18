#!/usr/bin/env python3
#
# In this script boat sails on given azimuth
#

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import MagneticField
import math
from std_msgs.msg import Float64


class Azimuth_node(Node):
    def __init__(self):
        super().__init__('Azimuth_node')

        self.given_azimuth = 300.0
        self.v = 0.3
        self.d = 0.0
        self.left_thrust = 0.0
        self.right_thrust = 0.0

        self.azimuth = 0.0
        self.e = 0
        self.p = 0.01 # parametr regulatora P
        self.mag_x = 0.0 
        self.mag_y = 0.0
        self.mag_z = 0.0 

        # Subskrybujemy topic /magnetometer
        self.subscription = self.create_subscription(
            MagneticField,
            '/magnetometer',
            self.mag_callback,
            10
        )
        self.get_logger().info("Magnetometer subscriber started!")

        # publishery na silniki
        self.left_pub = self.create_publisher(Float64, '/left_thrust', 10)
        self.right_pub = self.create_publisher(Float64, '/right_thrust', 10)


        # timer gdzie sie dzieje cala magia
        self.timer = self.create_timer(0.1, self.control_loop)

    def mag_callback(self, msg: MagneticField):
        # Aktualne wskazania w teslach
        # self.get_logger().info(
        #     f"Magnetic field -> X: {msg.magnetic_field.x:.6f} T, "
        #     f"Y: {msg.magnetic_field.y:.6f} T, "
        #     f"Z: {msg.magnetic_field.z:.6f} T"
        # )

        self.mag_x = msg.magnetic_field.x
        self.mag_y = msg.magnetic_field.y
        self.mag_z = msg.magnetic_field.z

        azimuth_rad = math.atan2(self.mag_y, self.mag_x)
        self.azimuth = math.degrees(azimuth_rad)
        # Normalizacja do 0-360°
        if self.azimuth < 0:
            self.azimuth += 360.0

        # Aktualny azymut
        # self.get_logger().info(f"Azimuth: {self.azimuth}")


    def publish_thrust(self):
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


    def control_loop(self):

        # licze blad normalizujac bo w stopniach jest modulo 360
        self.e = (self.given_azimuth - self.azimuth + 180) % 360 - 180

        # steruje wartoscia d (skret) regulatorem P
        self.d = self.e * self.p

        # ustawiam ciag na silnikach
        self.publish_thrust()
        

        # Logowanie lub publikacja
        self.get_logger().info("-------------------------------------------------------")
        self.get_logger().info(f"Given: {self.given_azimuth}°, Azymut: {self.azimuth:.2f}°, e = {self.e:.2f}°")
        self.get_logger().info(f"d: {self.d:.2f}%, v: {self.v}%, T_L: {self.left_thrust:.2f}%, T_R: {self.right_thrust:.2f}%")




def main(args=None):
    rclpy.init(args=args)
    node = Azimuth_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
