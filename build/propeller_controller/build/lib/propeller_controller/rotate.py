#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ThrustPublisher(Node):
    def __init__(self):
        super().__init__('right_thrust_pub')
        self.publisher_ = self.create_publisher(Float64, '/right_thrust', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz
        self.thrust_value = 1.0  # od 0 do 1

    def timer_callback(self):
        msg = Float64()
        msg.data = self.thrust_value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publikuję thrust={msg.data} na /right_thrust')

def main(args=None):
    rclpy.init(args=args)
    node = ThrustPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
