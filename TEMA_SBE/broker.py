import paho.mqtt.client as mqtt

window_size = 5
publication_window = []
connected_clients = []
subscriptions = []
publications = []
matches = {}

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
  # print("Received publication:", message)
  if "PUBLISHER" in message:
    publications.append(message.replace('PUBLISHER', ''))
    publication_window.append(message)
  else:
    subscriptions.append(message.replace('SUBSCRIBER', ''))
  if match_subscription(msg.topic, message):
    print("Message matches subscription:", message)
  if len(publication_window) >= window_size:
    process_publication_window()

def match_subscription(topic, message):
  for subscription in subscriptions:
    matches[subscription] = condition_matches(publications, subscription)

def condition_matches(publications, subscription):
  for publication in publications:
    all_conditions_match = True
    for condition in subscription:
      field, operator, value = condition.split(',')
      field_value = publication.get(field.strip())
      
      if operator.strip() == '=':
        if field_value != value.strip():
          all_conditions_match = False
          break
      elif operator.strip() == '!=':
        if field_value == value.strip():
          all_conditions_match = False
          break
      elif operator.strip() == '<':
        if not (field_value < float(value.strip())):
            all_conditions_match = False
            break
      elif operator.strip() == '<=':
        if not (field_value <= float(value.strip())):
          all_conditions_match = False
          break
      elif operator.strip() == '>':
        if not (field_value > float(value.strip())):
          all_conditions_match = False
          break
      elif operator.strip() == '>=':
        if not (field_value >= float(value.strip())):
          all_conditions_match = False
          break
      else:
        all_conditions_match = False
        break
    
    if all_conditions_match:
      return True

  return False

def notify_subscribers(message):
  print("Sending notification to subscribers:", message)
  for client in connected_clients:
    send_message(client, message)

def process_publication_window():
  print("Processing publication window:", publication_window)
  print('publications', publications)
  print('subscriptions', subscriptions)
  print('publication_window', publication_window)
  publication_window.clear()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_new_client = on_new_client

client2 = mqtt.Client()
client2.on_connect = on_connect
client2.on_message = on_message
client2.on_new_client = on_new_client

client3 = mqtt.Client()
client3.on_connect = on_connect
client3.on_message = on_message
client3.on_new_client = on_new_client

client.connect("localhost", 1883)
client2.connect("localhost", 1884)
client2.connect("localhost", 1885)

client.loop_forever()
client2.loop_forever()
client3.loop_forever()
