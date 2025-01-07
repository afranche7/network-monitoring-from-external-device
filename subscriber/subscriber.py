from influx_client import insert_measurements
from paho.mqtt import client as mqtt
import json


def on_message(client, userdata, message):
    try:
        decoded_payload = message.payload.decode("utf-8")
        metrics = json.loads(decoded_payload)
        insert_measurements(metrics["ping"])
    except:
        pass


client = mqtt.Client(client_id="Subscriber", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("mqtt-broker", 1883)
client.subscribe("test/topic")
client.on_message = on_message
client.loop_forever()
