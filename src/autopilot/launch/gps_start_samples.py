#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import csv
import statistics
from datetime import datetime

class GPSAverage(Node):
    def __init__(self):
        super().__init__('gps_average_node')
        self.subscription = self.create_subscription(
            NavSatFix,
            '/gps/fix',
            self.gps_callback,
            10
        )

        # listy pomiarów
        self.latitudes = []
        self.longitudes = []
        self.altitudes = []
        self.num_samples = 100

        # przygotuj plik CSV z timestampem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.csv_filename = f"gps_log_{timestamp}.csv"

        with open(self.csv_filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["# latitude", "longitude", "altitude"])

        self.get_logger().info(f"📁 Dane GPS będą zapisywane do: {self.csv_filename}")

    def gps_callback(self, msg: NavSatFix):
        if msg.status.status < 0:
            self.get_logger().warn('⚠️  Brak fixa GPS — pomiar pominięty')
            return

        # zapisz dane
        self.latitudes.append(msg.latitude)
        self.longitudes.append(msg.longitude)
        self.altitudes.append(msg.altitude)

        with open(self.csv_filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([msg.latitude, msg.longitude, msg.altitude])

        self.get_logger().info(f"📡 Pomiar {len(self.latitudes)}/{self.num_samples} zapisany")

        # gdy zebrano komplet
        if len(self.latitudes) >= self.num_samples:
            lat_avg = statistics.mean(self.latitudes)
            lon_avg = statistics.mean(self.longitudes)
            alt_avg = statistics.mean(self.altitudes)

            self.get_logger().info(f"\n✅ Średnie współrzędne GPS z {self.num_samples} pomiarów:")
            self.get_logger().info(f"  latitude:  {lat_avg:.8f}")
            self.get_logger().info(f"  longitude: {lon_avg:.8f}")
            self.get_logger().info(f"  altitude:  {alt_avg:.3f}")

            self.get_logger().info(f"\n📌 Możesz wpisać do pliku konfiguracyjnego:")
            self.get_logger().info(f"datum: [{lat_avg:.8f}, {lon_avg:.8f}, {alt_avg:.3f}]")

            self.get_logger().info(f"\n📁 Wszystkie pomiary zapisane w: {self.csv_filename}")
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = GPSAverage()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("⏹️ Zatrzymano pomiar GPS (Ctrl+C).")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
