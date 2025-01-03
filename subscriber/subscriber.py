from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    print(f"Received: {message.payload.decode()}")


client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2, client_id="Subscriber")
client.connect("localhost", 1883)
client.subscribe("test/topic")
client.on_message = on_message
client.loop_forever()
