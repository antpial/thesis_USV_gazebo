#!/usr/bin/env python3

# ** MY CUSTOM ROS2 <-> GZ SIM BRIDGE **


import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

import gz.transport13 as gz
from gz.msgs10.double_pb2 import Double
from gz.msgs10.magnetometer_pb2 import Magnetometer
from gz.msgs10.vector3d_pb2 import Vector3d
from gz.msgs10.navsat_pb2 import NavSat
from gz.msgs10.imu_pb2 import IMU as gzImu

from sensor_msgs.msg import MagneticField
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu




class RosGzBridge(Node):
    def __init__(self):
        super().__init__('ros_gz_bridge_custom')

        # --- ROS Subscribers ---
        self.subscription = self.create_subscription(
            Float64,
            '/right_thrust',
            self.right_thrust_callback,
            10
        )

        self.subscription = self.create_subscription(
            Float64,
            '/left_thrust',
            self.left_thrust_callback,
            10
        )

        self.subscription = self.create_subscription(
            NavSatFix,
            '/gps/filtered',
            self.gps_filtered_callback,
            10
        )

        # --- ROS publishers ----

        self.ros_mag_pub = self.create_publisher(
            MagneticField,
            '/magnetometer',
            10
        )

        self.ros_gps_pub = self.create_publisher(
            NavSatFix,
            '/gps/fix',
            10
        )

        self.ros_perfect_gps_pub = self.create_publisher(
            NavSatFix,
            '/gps/perfect',
            10
        )

        self.ros_imu_pub = self.create_publisher(
            Imu,
            '/imu',
            10
        )


        self.gz_node = gz.Node()

        # --- Gazebo Subscribers ---

        if not self.gz_node.subscribe(Magnetometer, "/wamv/magnetometer", self.mag_callback):
            self.get_logger().error("Can not subscribe /wamv/magnetometer!")
            return

        if not self.gz_node.subscribe(NavSat, "/wamv/gps", self.gps_callback):
            self.get_logger().error("Cannot subscribe /wamv/gps!")
            return
        
        if not self.gz_node.subscribe(NavSat, "/wamv/gps/perfect", self.perfect_gps_callback):
            self.get_logger().error("Cannot subscribe /wamv/gps/perfect!")
            return
        
        if not self.gz_node.subscribe(gzImu, "/wamv/imu", self.imu_callback):
            self.get_logger().error("Cannot subscribe /wamv/imu!")
            return


        # --- Gazebo Publisher ---

        #Node do debugingu lokalizacji w gazebo
        self.gz_pub_gps_filtered = self.gz_node.advertise(
            '/gz/gps/filtered',
            NavSat
        )

        self.gz_pub_right_thrust = self.gz_node.advertise(
            '/model/wam-V/joint/right_engine_propeller_joint/cmd_thrust',
            Double
        )

        self.gz_pub_left_thrust = self.gz_node.advertise(
            '/model/wam-V/joint/left_engine_propeller_joint/cmd_thrust',
            Double
        )

        self.get_logger().info("Mostek ROS ↔ Gazebo uruchomiony!")


    # All callbacks

    def gps_filtered_callback(self, msg: NavSatFix):
        # Przekazuje przefiltrowane dane GPS z ROS do Gazebo (do debugowania)
        gz_msg = NavSat()
        gz_msg.latitude_deg = msg.latitude
        gz_msg.longitude_deg = msg.longitude
        gz_msg.altitude = msg.altitude
        self.gz_pub_gps_filtered.publish(gz_msg)
        self.get_logger().info(f"Przekazuję {msg.latitude}, {msg.longitude}, {msg.altitude} z ROS → Gazebo")


    def right_thrust_callback(self, msg: Float64):
        gz_msg = Double()
        gz_msg.data = msg.data * 13.0 * 9.81 # F = (max thrust dla 18V na stronie prod.) * g
        self.gz_pub_right_thrust.publish(gz_msg)
        # self.get_logger().info(f"Przekazuję {msg.data} z ROS → Gazebo")


    def left_thrust_callback(self, msg: Float64):
        gz_msg = Double()
        gz_msg.data = msg.data * 13.0 * 9.81 # F = (max thrust dla 18V na stronie prod.) * g
        self.gz_pub_left_thrust.publish(gz_msg)
        # self.get_logger().info(f"Przekazuję {msg.data} z ROS → Gazebo")
    

    def mag_callback(self, msg: Magnetometer):
        # Convert Gazebo Magnetometer message to ROS MagneticField message
        ros_msg = MagneticField()
        
        # Set header with current time
        ros_msg.header.stamp = self.get_clock().now().to_msg()
        ros_msg.header.frame_id = "magnetometer_frame"  # You can change this as needed
        
        # Convert magnetic field data
        ros_msg.magnetic_field.x = msg.field_tesla.x
        ros_msg.magnetic_field.y = msg.field_tesla.y
        ros_msg.magnetic_field.z = msg.field_tesla.z
        
        # Publish ROS message
        self.ros_mag_pub.publish(ros_msg)
        # self.get_logger().info(f"Received magnetometer data: x={msg.field_tesla.x}, y={msg.field_tesla.y}, z={msg.field_tesla.z}")

    def imu_callback(self, msg: gzImu):
        imu_msg = Imu()
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.header.frame_id = "imu_link"
        # mapowanie pól z Gazebo -> ROS2
        imu_msg.orientation.x = msg.orientation.x
        imu_msg.orientation.y = msg.orientation.y
        imu_msg.orientation.z = msg.orientation.z
        imu_msg.orientation.w = msg.orientation.w

        imu_msg.angular_velocity.x = msg.angular_velocity.x
        imu_msg.angular_velocity.y = msg.angular_velocity.y
        imu_msg.angular_velocity.z = msg.angular_velocity.z

        imu_msg.linear_acceleration.x = msg.linear_acceleration.x
        imu_msg.linear_acceleration.y = msg.linear_acceleration.y
        imu_msg.linear_acceleration.z = msg.linear_acceleration.z

        # --- KOWARIANCJE ---
        imu_msg.orientation_covariance = [
            0.0025, 0, 0,
            0, 0.0025, 0,
            0, 0, 0.0025
        ]
        imu_msg.angular_velocity_covariance = [
            0.0001, 0, 0,
            0, 0.0001, 0,
            0, 0, 0.0001
        ]
        imu_msg.linear_acceleration_covariance = [
            0.04, 0, 0,
            0, 0.04, 0,
            0, 0, 0.04
        ]

        self.ros_imu_pub.publish(imu_msg)


    def gps_callback(self, msg: NavSat):
        navsat_msg = NavSatFix()
        navsat_msg.header.stamp = self.get_clock().now().to_msg()
        navsat_msg.header.frame_id = "gps_link"
        # mapowanie pól z Gazebo -> ROS2
        navsat_msg.latitude = msg.latitude_deg
        navsat_msg.longitude = msg.longitude_deg
        navsat_msg.altitude = msg.altitude

        # opcjonalnie: status
        from sensor_msgs.msg import NavSatStatus
        navsat_msg.status.status = NavSatStatus.STATUS_FIX
        navsat_msg.status.service = NavSatStatus.SERVICE_GPS

        # Kowariancje pozycji
        CEP = 2.0  # Circular Error Probable w metrach
        sigma_h = CEP * 0.847 # przekształcenie CEP na sigma (przybliżenie)
        sigma_z = 3.0   # pionowa sigma w metrach (zmień wg sprzętu)

        var_x = sigma_h ** 2
        var_y = sigma_h ** 2
        var_z = sigma_z ** 2

        # Pozycja — zapisz macierz diagonalną (row-major 3x3)
        navsat_msg.position_covariance = [
            var_x, 0.0,   0.0,
            0.0,   var_y, 0.0,
            0.0,   0.0,   var_z
        ]
        # Powiedzemy, że znamy diagonalne elementy
        navsat_msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_DIAGONAL_KNOWN


        self.ros_gps_pub.publish(navsat_msg)


    def perfect_gps_callback(self, msg: NavSat):
        navsat_msg = NavSatFix()
        navsat_msg.header.stamp = self.get_clock().now().to_msg()
        navsat_msg.header.frame_id = "perfect_gps_link"
        # mapowanie pól z Gazebo -> ROS2
        navsat_msg.latitude = msg.latitude_deg
        navsat_msg.longitude = msg.longitude_deg
        navsat_msg.altitude = msg.altitude

        self.ros_perfect_gps_pub.publish(navsat_msg)




def main(args=None):
    rclpy.init(args=args)
    node = RosGzBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
