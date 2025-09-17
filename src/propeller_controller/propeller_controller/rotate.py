#!/usr/bin/env python3
import time
import gz.transport13 as gz
from gz.msgs10.double_pb2 import Double  # <-- tu używamy wersji 10

def main():
    node = gz.Node()

    topic = "/model/wam-V/joint/right_engine_propeller_joint/cmd_thrust"

    pub = node.advertise(topic, Double)

    msg = Double()
    msg.data = 10.0

    print(f"Publikuję thrust={msg.data} na {topic}")
    while True:
        pub.publish(msg)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
