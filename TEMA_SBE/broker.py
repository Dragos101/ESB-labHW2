import paho.mqtt.client as mqtt

window_size = 5
publication_window = []
connected_clients = []
subscriptions = []

def on_new_client(client, userdata, flags, rc):
  print("New client connected:", client)
  connected_clients.append(client)

def send_message(client, message):
  client.publish("topic", message)

def on_connect(client, userdata, flags, rc):
  print("Connected: " + str(rc))
  client.subscribe("topic")

def on_message(client, userdata, msg):
  message = msg.payload.decode()
  subscriptions.append(message)
  if match_subscription(msg.topic, message):
    print("Message matches subscription:", message)
  publication_window.append(message)
  # if len(publication_window) >= window_size:
  #   process_publication_window()

def match_subscription(topic, message):
  for subscription in subscriptions:
    if all(condition_matches(subscription_condition, message) for subscription_condition in subscription):
      return True
  return False

def condition_matches(condition, message):
  print('ici', condition)
  print('cava', message)
  # field, operator, value = condition.split(',')
  # field_value = message.get(field.strip())
  # if operator.strip() == '=':
  #   return field_value == value.strip()
  # elif operator.strip() == '!=':
  #   return field_value != value.strip()
  # elif operator.strip() == '<':
  #   return field_value < float(value.strip())
  # elif operator.strip() == '<=':
  #   return field_value <= float(value.strip())
  # elif operator.strip() == '>':
  #   return field_value > float(value.strip())
  # elif operator.strip() == '>=':
  #   return field_value >= float(value.strip())
  # else:
  return False

def notify_subscribers(message):
  print("Sending notification to subscribers:", message)
  for client in connected_clients:
    send_message(client, message)

def process_publication_window():
  print("Processing publication window:", publication_window)
  publication_window.clear()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_new_client = on_new_client


client.connect("localhost", 1883)

client.loop_forever()
