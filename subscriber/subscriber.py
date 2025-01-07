from influx_client import insert_measurements
from paho.mqtt import client as mqtt
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def on_message(client, userdata, message):
    decoded_payload = message.payload.decode("utf-8")
    logger.info(f"Received: {decoded_payload}")
    metrics = json.loads(decoded_payload)
    insert_measurements(metrics["ping"])


client = mqtt.Client(client_id="Subscriber", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("mqtt-broker", 1883)
client.subscribe("test/topic")
client.on_message = on_message
client.loop_forever()
