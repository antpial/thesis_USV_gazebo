import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from rclpy.time import Time
import os
import csv
import sys


class GpsComparator(Node):

    def __init__(self, csv_filename):
        super().__init__('gps_comparator')

        self.sub_fix = self.create_subscription(
            NavSatFix, '/gps/filtered', self.cb_fix, 10)

        self.sub_fix_perfect = self.create_subscription(
            NavSatFix, '/gps/perfect', self.cb_fix_perfect, 10)

        # Bufory wiadomości
        self.buffer_fix = []
        self.buffer_perf = []

        # Nazwa pliku
        self.csv_directory = "Sim_output"
        self.csv_filename = os.path.join(self.csv_directory, csv_filename)

        # Jeśli plik nie istnieje — utwórz nagłówki
        self.create_csv_if_not_exist()

    def create_csv_if_not_exist(self):
        if not os.path.exists(self.csv_filename):
            with open(self.csv_filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp_fix_sec",
                    "timestamp_fix_nanosec",
                    "timestamp_perf_sec",
                    "timestamp_perf_nanosec",
                    "lat_fix",
                    "lon_fix",
                    "alt_fix",
                    "lat_perf",
                    "lon_perf",
                    "alt_perf",
                    "lat_error",
                    "lon_error",
                    "alt_error"
                ])

    def cb_fix(self, msg):
        self.buffer_fix.append(msg)
        self.compare_if_possible()

    def cb_fix_perfect(self, msg):
        self.buffer_perf.append(msg)
        self.compare_if_possible()

    def compare_if_possible(self):
        if len(self.buffer_fix) == 0 or len(self.buffer_perf) == 0:
            return

        msg_fix = self.buffer_fix[-1]
        msg_perf = self.buffer_perf[-1]

        t_fix = Time.from_msg(msg_fix.header.stamp)
        t_perf = Time.from_msg(msg_perf.header.stamp)

        time_diff = abs((t_fix - t_perf).nanoseconds)

        # Dopasowanie czasowe < 100 ms
        if time_diff < 1e8:
            self.write_csv(msg_fix, msg_perf)

    def write_csv(self, msg_fix, msg_perf):

        lat_error = msg_fix.latitude - msg_perf.latitude
        lon_error = msg_fix.longitude - msg_perf.longitude
        alt_error = msg_fix.altitude - msg_perf.altitude

        with open(self.csv_filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                msg_fix.header.stamp.sec,
                msg_fix.header.stamp.nanosec,
                msg_perf.header.stamp.sec,
                msg_perf.header.stamp.nanosec,
                msg_fix.latitude,
                msg_fix.longitude,
                msg_fix.altitude,
                msg_perf.latitude,
                msg_perf.longitude,
                msg_perf.altitude,
                lat_error,
                lon_error,
                alt_error
            ])

        self.get_logger().info(f"Dodano wpis do CSV ({self.csv_filename})")


def main(args=None):
    rclpy.init(args=args)

    # Argument pliku CSV
    if len(sys.argv) > 1:
        csv_filename = sys.argv[1]
    else:
        csv_filename = "gps_compare_output.csv"

    node = GpsComparator(csv_filename)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
