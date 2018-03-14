
#https://www.youtube.com/watch?v=vT4FTRgipOM
import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print "Connected OK"
	print "Bad connection Returned code = ", rc
broker = "192.168.1.184"
client = mqtt.Client("Python1") #create new instance of mqtt
"""for i in client.__dict__:
	print i
"""

client.on_connect = on_connect #bind call function
print "Connecting to broker", broker
client.loop_start()  #start loop
client.connect(broker) #connect to broker
client.publish("house/main-light",  "off") #publishes "off" message to "house/main-light" topic
time.sleep(4)
client.loop_stop()  #stops loop
client.disconnect() # disconnects
print "-----"