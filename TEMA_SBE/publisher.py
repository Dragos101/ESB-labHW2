import time
import paho.mqtt.client as mqtt
import publications as pub

broker_host = "localhost"
broker_port = 1883

publisher = mqtt.Client("Publisher")
publisher.connect(broker_host, broker_port)

publications = pub.Publication().generate_publications(5)

for publication in publications:
    print(publication)
    message = "PUBLISHER: " + str(publication)  # Add "SUBSCRIBER: " prefix to the message

    publisher.publish("topic", message)
    time.sleep(1)

publisher.disconnect()
