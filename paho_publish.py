#paho_publish.py
import time
import paho.mqtt.client as mqtt
broker = "172.24.223.27"
client =mqtt.Client("TID-2182497-320000001")
client.connect(broker)


for i in range(1000):
	time.sleep(20)
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LLLLL")


print 
"""for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)


for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)
for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)


for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)

for i in range(1000):
	client.publish("/gateways/ontrackgl/TID-2182497-320000001/config", "LALALA"*10000000)
"""