import rclpy
from rclpy.node import Node
from sensor_msgs.msg import MagneticField
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import math
import math

def euler_to_quaternion(roll, pitch, yaw):
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    q = [
        sr * cp * cy - cr * sp * sy,  # x
        cr * sp * cy + sr * cp * sy,  # y
        cr * cp * sy - sr * sp * cy,  # z
        cr * cp * cy + sr * sp * sy   # w
    ]
    return q


class CompassOdomNode(Node):
    def __init__(self):
        super().__init__('compass_odom_node')

        # Parametry
        self.declare_parameter('mag_topic', '/magnetometer')
        self.declare_parameter('publish_topic', '/odometry/yaw')
        self.declare_parameter('frame_id', 'odom')
        self.declare_parameter('child_frame_id', 'magnetometer_link')

        self.mag_topic = self.get_parameter('mag_topic').get_parameter_value().string_value
        self.publish_topic = self.get_parameter('publish_topic').get_parameter_value().string_value
        self.frame_id = self.get_parameter('frame_id').get_parameter_value().string_value
        self.child_frame_id = self.get_parameter('child_frame_id').get_parameter_value().string_value

        # Publisher
        self.pub = self.create_publisher(Odometry, self.publish_topic, 10)

        # Subskrypcja magnetometru
        self.mag_sub = self.create_subscription(MagneticField, self.mag_topic, self.mag_callback, 10)

    def mag_callback(self, msg: MagneticField):
        mx = msg.magnetic_field.x
        my = msg.magnetic_field.y

        # Heading w płaszczyźnie XY (bez tilt compensation)
        yaw = math.atan2(-my, mx)
        quat = euler_to_quaternion(0.0, 0.0, yaw)

        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = self.frame_id
        odom_msg.child_frame_id = self.child_frame_id

        # Pozycja zerowa
        odom_msg.pose.pose.position.x = 0.0
        odom_msg.pose.pose.position.y = 0.0
        odom_msg.pose.pose.position.z = 0.0

        # Orientacja z yaw
        odom_msg.pose.pose.orientation = Quaternion(
            x=quat[0],
            y=quat[1],
            z=quat[2],
            w=quat[3]
        )

        # Covariance – możesz ustawić np. na 0.1 rad^2 dla yaw
        odom_msg.pose.covariance = [
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.01  # yaw covariance
        ]

        self.pub.publish(odom_msg)
        self.get_logger().debug(f"Heading published: {math.degrees(yaw):.2f}°")


def main(args=None):
    rclpy.init(args=args)
    node = CompassOdomNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
