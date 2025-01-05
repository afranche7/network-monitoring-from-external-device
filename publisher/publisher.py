import time
import json
from network_monitor import NetworkMonitor
from paho.mqtt import client as mqtt

client = mqtt.Client(client_id="Publisher", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

client.connect("mqtt-broker", 1883)
while True:
    monitor = NetworkMonitor()
    monitor.start()
    client.publish("test/topic", json.dumps(monitor.get_metrics()))
    time.sleep(5)
