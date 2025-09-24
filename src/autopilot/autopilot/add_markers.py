#!/usr/bin/env python3
import time
import gz.msgs10.marker_pb2 as marker_msg
import gz.transport13 as gz

def main():
    # Tworzymy node transportu
    node = gz.Node()

    # Publisher na topic /marker
    pub = node.advertise("/marker", marker_msg.Marker)

    # Tworzymy marker
    marker = marker_msg.Marker()
    marker.id = 1
    marker.ns = "visual_cube"
    marker.type = 1      # 0=SPHERE, 1=CUBE, 2=CYLINDER itd.
    marker.action = 0    # 0=ADD
    marker.pose.position.x = 0.0
    marker.pose.position.y = 0.0
    marker.pose.position.z = 0.5
    marker.pose.orientation.w = 1.0
    marker.scale.x = 1.0
    marker.scale.y = 1.0
    marker.scale.z = 1.0

    # Kolor
    marker.material.ambient.r = 0.0
    marker.material.ambient.g = 1.0
    marker.material.ambient.b = 0.0
    marker.material.ambient.a = 0.5
    marker.material.diffuse.r = 0.0
    marker.material.diffuse.g = 1.0
    marker.material.diffuse.b = 0.0
    marker.material.diffuse.a = 0.5

    # Pętla publikująca marker co sekundę
    while True:
        pub.publish(marker)
        print("Marker published!")
        time.sleep(1)

if __name__ == "__main__":
    main()
