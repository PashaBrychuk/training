import requests
from urllib2 import urlopen
print "111111"
url = "http://demo-wds-uat.wdsserve.com/api/atom/demo?dialog=va"
va = urlopen(url)
response  = va.read()
print response
""""print "!!!!!!!!!!!!!!!"
kittens = requests.get("http://placekitten.com/")
print kittens.text"""