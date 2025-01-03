import asyncio
import time

from paho.mqtt.enums import CallbackAPIVersion
from network_monitor import NetworkMonitor
import paho.mqtt.client as mqtt

# if __name__ == "__main__":
#     async def main():
#         monitor = NetworkMonitor()
#         await monitor.analyze()
#         print("Ping Metrics:", monitor.ping_metrics)
#         print("Speed Metrics:", monitor.speed_metrics)
#
#
#     asyncio.run(main())

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2, client_id="Publisher")

client.connect("localhost", 1883)
while True:
    client.publish("test/topic", "Hello from MQTT Docker!")
    print("Message sent!")
    time.sleep(5)
