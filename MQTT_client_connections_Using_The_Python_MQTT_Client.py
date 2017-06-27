#https://www.youtube.com/watch?v=vT4FTRgipOM
import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print "Connected OK"
	print "Bad connection Returned code = ", rc
broker = "192.168.1.184"
client = mqtt.Client("Python1")
for i in client.__dict__:
	print i