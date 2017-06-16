import urllib
import webbrowser
webbrowser.open("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
print type(webbrowser.open("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"))
u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
data = u.read()
print data
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

daves_lat = 41.98062
daves_long = -87.668452
candidates = []
from  xml.etree.ElementTree import parse
doc = parse('rt22.xml')
count = 0
for bus in doc.findall('bus'): 
	lat = float(bus.findtext('lat'))
	if lat > daves_lat:
		direction  = bus.findtext("North")
		busid = bus.findtext('id')
		print busid, lat
		count = count + 1
		candidates.append(busid)

print count
print candidates

def distance(lat1, lat2):
	return 69 * abs(lat1-lat2)
def monitor():
	u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
	doc = parse(u)
	for bus in doc.findall('bus'):
		busid = bus.findtext('id')
		if busid in candidates:
			lat = float(bus.findtext('lat'))
			dis = distance(lat, daves_lat)
			print busid, dis, 'miles'

import time
while True:
	monitor()
	time.sleep(60)
	print "------------------------"
