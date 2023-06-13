import time
import paho.mqtt.client as mqtt
import subscriptions as sub

def on_connect(client, userdata, flags, rc):
    print("Connected: " + str(rc))
    client.subscribe("topic")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    process_message(message)

def process_message(message):
    print("Received message:", message)

client1 = mqtt.Client()
client1.on_connect = on_connect
client1.on_message = on_message

client1.connect('localhost', 1883)
client1.loop_start()

client2 = mqtt.Client()
client2.on_connect = on_connect
client2.on_message = on_message

client2.connect('localhost', 1883)
client2.loop_start()

client3 = mqtt.Client()
client3.on_connect = on_connect
client3.on_message = on_message

client3.connect('localhost', 1883)
client3.loop_start()

subscriptions = sub.Subscription().generate_objects(5)

for i in range(0, 5):
  client1.publish("topic", str(subscriptions[i]))
  # client2.publish("topic", str(subscriptions))
  # client3.publish("topic", str(subscriptions))
  time.sleep(1)

time.sleep(5)

client1.disconnect()
client2.disconnect()
client3.disconnect()
