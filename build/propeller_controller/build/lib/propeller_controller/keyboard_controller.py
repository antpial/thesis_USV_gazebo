#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import sys
import termios
import tty
import select


def get_key(settings):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


class ThrusterController(Node):
    def __init__(self):
        super().__init__('thruster_controller')

        # publisher’y
        self.left_pub = self.create_publisher(Float64, '/left_thrust', 10)
        self.right_pub = self.create_publisher(Float64, '/right_thrust', 10)

        # wartości początkowe
        self.left_thrust = 0.0
        self.right_thrust = 0.0
        self.v = 0.0
        self.d = 0.0

        # timer do cyklicznego publikowania
        self.timer = self.create_timer(0.1, self.publish_thrust)  # 10 Hz

    def publish_thrust(self):
        msg_left = Float64()
        msg_right = Float64()

        if(self.d <= 0):
            self.left_thrust = self.v * (1 + 2 * self.d)
            self.right_thrust = self.v
        else:
            self.left_thrust = self.v
            self.right_thrust = self.v * (1 - 2 * self.d)

        msg_left.data = self.left_thrust
        msg_right.data = self.right_thrust

        self.left_pub.publish(msg_left)
        self.right_pub.publish(msg_right)

        self.get_logger().info(f'Lewy={msg_left.data:.2f}, Prawy={msg_right.data:.2f}')

    def handle_key(self, key):
        if key == '\x1b':  # strzałki zaczynają się od ESC
            seq = sys.stdin.read(2)
            if seq == '[A':  # strzałka w górę
                self.v += 0.1
                self.get_logger().info(f"Stzralka w gore! v = {self.v}")
            elif seq == '[B':  # strzałka w dół
                self.v -= 0.1
                self.get_logger().info(f"Stzralka w dol! v = {self.v}")
            elif seq == '[C':  # strzałka w prawo
                self.d += 0.1
                self.get_logger().info(f"Stzralka w prawo! d = {self.d}")
            elif seq == '[D':  # strzałka w lewo
                self.d -= 0.1
                self.get_logger().info(f"Stzralka w lewo! d = {self.d}")
        elif key.lower() == 'r':
            # reset thrust
            self.v = 0.0
            self.d = 0.0
            self.get_logger().info('Reset thrust → v = 0.0, d = 0.0')
        elif key.lower() == 'e':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
            node.destroy_node()
            rclpy.shutdown()


def show_manual():
    print("---------- MANUAL ---------")
    print("strzalka w gore:  v + 10 p.p.")
    print("strzalka w dol:   v - 10 p.p.")
    print("strzalka w prawo: d + 10 p.p.")    
    print("strzalka w lewo:  d - 10 p.p.")
    print("r:                v = 0,")
    print("                  d = 0")
    print("e:                exit")
    print("---------------------------")




def main(args=None):
    rclpy.init(args=args)
    node = ThrusterController()

    settings = termios.tcgetattr(sys.stdin)

    show_manual()

    try:
        while rclpy.ok():
            key = get_key(settings)
            if key:
                node.handle_key(key)
            rclpy.spin_once(node, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
