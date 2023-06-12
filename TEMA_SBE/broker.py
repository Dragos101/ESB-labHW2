import paho.mqtt.client as mqtt

window_size = 5
publication_window = []

# Callback function for the connect event
def on_connect(client, userdata, flags, rc):
  print("Connected: " + str(rc))
  # Subscribe to the desired topic for receiving publications
  client.subscribe("topic")

# Callback function for the message event
def on_message(client, userdata, msg):
  # Decode the message
  message = msg.payload.decode()
  # Check for subscription match
  if match_subscription(message):
    print("Message matches subscription:", message)

# Function to check subscription match (placeholder implementation)
def match_subscription(message):
  return True

# Set up the MQTT client and callback functions
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect the client to the brokers
client.connect("localhost", 1883)
client.connect("localhost", 1884)
client.connect("localhost", 1885)

# Start the client's network loop (blocking call)
client.loop_forever()
