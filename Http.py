import requests
from urllib2 import urlopen
print "111111"
url = "http://demo-wds-uat.wdsserve.com/api/atom/demo?dialog=va"
va = urlopen(url)
print va
print type(va)
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
response = va.read()
print response













"""url = "http://event-tracker-uat.wdsserve.com/event-tracker-server/v3/conversations?contentGroup=638&startDate=2017-03-15T00:00:00.000Z&endDate=2017-03-26T00:00:00.000Z"
va = urlopen(url)
response  = va.read()
print response
"""
"""print "!!!!!!!!!!!!!!!"
kittens = requests.get("http://placekitten.com/")
print kittens.text"""