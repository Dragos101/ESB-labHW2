import time
import paho.mqtt.client as mqtt
import subscriptions as sub

# Callback function pentru evenimentul de conectare la broker
def on_connect(client, userdata, flags, rc):
  print("Connected: " + str(rc))
  # Abonarea la topicul dorit pentru primirea publicațiilor
  client.subscribe("topic")

# Callback function pentru evenimentul de primire a unui mesaj de la broker
def on_message(client, userdata, msg):
  # Decodificarea mesajului
  message = msg.payload.decode()
  # Procesarea mesajului
  process_message(message)

# Funcție pentru procesarea mesajului primit
def process_message(message):
  print("Received message:", message)
  # Implement your actions based on the message content

# Setarea callback-urilor de conectare și primire a mesajelor de la broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectarea clientului la broker
client.connect("localhost", 1887)

# Pornirea buclei principale pentru a menține conexiunea cu brokerul
client.loop_start()

# Simularea nodurilor subscriber
subscriptions = sub.Subscription().generate_objects(5)
print(subscriptions)
for subscription in subscriptions:
  # Register the subscription
  client.publish("topic", str(subscription))
  time.sleep(1)  # Pause between subscription registrations
