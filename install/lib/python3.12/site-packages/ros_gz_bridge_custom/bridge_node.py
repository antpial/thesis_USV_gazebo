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

from sensor_msgs.msg import MagneticField
from sensor_msgs.msg import NavSatFix




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

        # --- ROS publishers ----

        self.ros_mag_pub = self.create_publisher(
            MagneticField,
            '/magnetometer',
            10
        )

        self.ros_gps_pub = self.create_publisher(
            NavSatFix,
            '/gps',
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


        # --- Gazebo Publisher ---
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

    def right_thrust_callback(self, msg: Float64):
        gz_msg = Double()
        gz_msg.data = msg.data * 4.79 * 9.81 # F = (max thrust dla 18V na stronie prod.) * g
        self.gz_pub_right_thrust.publish(gz_msg)
        self.get_logger().info(f"Przekazuję {msg.data} z ROS → Gazebo")


    def left_thrust_callback(self, msg: Float64):
        gz_msg = Double()
        gz_msg.data = msg.data * 4.79 * 9.81 # F = (max thrust dla 18V na stronie prod.) * g
        self.gz_pub_left_thrust.publish(gz_msg)
        self.get_logger().info(f"Przekazuję {msg.data} z ROS → Gazebo")
    

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



    def gps_callback(self, msg: NavSat):
        navsat_msg = NavSatFix()
        navsat_msg.header.stamp = self.get_clock().now().to_msg()
        navsat_msg.header.frame_id = msg.frame_id

        # mapowanie pól z Gazebo -> ROS2
        navsat_msg.latitude = msg.latitude_deg
        navsat_msg.longitude = msg.longitude_deg
        navsat_msg.altitude = msg.altitude

        # opcjonalnie: status
        from sensor_msgs.msg import NavSatStatus
        navsat_msg.status.status = NavSatStatus.STATUS_FIX
        navsat_msg.status.service = NavSatStatus.SERVICE_GPS

        self.ros_gps_pub.publish(navsat_msg)




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
