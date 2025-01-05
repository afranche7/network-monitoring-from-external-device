import time
import json
from paho.mqtt.enums import CallbackAPIVersion
from network_monitor import NetworkMonitor
import paho.mqtt.client as mqtt

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2, client_id="Publisher")

client.connect("mqtt-broker", 1883)
while True:
    monitor = NetworkMonitor()
    monitor.start()
    client.publish("test/topic", json.dumps(monitor.get_metrics()))
    time.sleep(5)
