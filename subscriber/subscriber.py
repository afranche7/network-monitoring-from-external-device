from paho.mqtt import client as mqtt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def on_message(client, userdata, message):
    logger.info(f"Received: {message.payload.decode()}")


client = mqtt.Client(client_id="Subscriber", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("mqtt-broker", 1883)
client.subscribe("test/topic")
client.on_message = on_message
client.loop_forever()
