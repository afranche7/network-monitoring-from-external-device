from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.client as mqtt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def on_message(client, userdata, message):
    logger.info(f"Received: {message.payload.decode()}")


client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2, client_id="Subscriber")
client.connect("mqtt-broker", 1883)
client.subscribe("test/topic")
client.on_message = on_message
client.loop_forever()
