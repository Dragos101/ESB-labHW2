import time
import paho.mqtt.client as mqtt
import publications as pub

# Initializarea clientului MQTT pentru publisher
publisher = mqtt.Client("Publisher")

# Conectarea la broker
publisher.connect("localhost", 1886)

# Definirea listei de publicații
publications = pub.Publication().generate_publications(5)
print(publications)

for publication in publications:
    publisher.publish("topic", str(publication))
    time.sleep(1)

# Deconectarea de la broker
publisher.disconnect()
