#!/usr/bin/env python3

# ** MY CUSTOM ROS2 <-> GZ SIM BRIDGE **

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

import gz.transport13 as gz
from gz.msgs10.double_pb2 import Double


class RosGzBridge(Node):
    def __init__(self):
        super().__init__('ros_gz_bridge_custom')

        # --- ROS Subscriber (odbieramy thrust od użytkownika/ROS) ---
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

        # --- Gazebo Publisher ---
        self.gz_node = gz.Node()
        self.gz_pub_right_thrust = self.gz_node.advertise(
            '/model/wam-V/joint/right_engine_propeller_joint/cmd_thrust',
            Double
        )

        self.gz_pub_left_thrust = self.gz_node.advertise(
            '/model/wam-V/joint/left_engine_propeller_joint/cmd_thrust',
            Double
        )

        self.get_logger().info("Mostek ROS ↔ Gazebo uruchomiony!")

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
