import time
import paho.mqtt.client as mqtt
import publications as pub

publisher = mqtt.Client("Publisher")

brokers = ["localhost", "localhost"]
ports = [1883, 1884]

for i in range(len(brokers)):
  publisher.connect(brokers[i], ports[i])
  time.sleep(1)

publications = pub.Publication().generate_publications(5)

for publication in publications:
  print(publication)
  publisher.publish("topic", str(publication))
  time.sleep(1)

publisher.disconnect()
