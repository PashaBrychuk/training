import urllib
import webbrowser
s = webbrowser.open("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
data = u.read()
print data
f = open('rt22.xml', 'wb')
f.write(data)
f.close()
