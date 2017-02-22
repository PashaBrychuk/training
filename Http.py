import requests
from urllib2 import urlopen
print "111111"
url = "http://placekitten.com/"
kits = urlopen(url)
response  = kits.read()
print response
print "!!!!!!!!!!!!!!!"
kittens = requests.get("http://placekitten.com/")
print kittens.text