import requests
from urllib2 import urlopen
print "111111"
url = "http://placekitten.com/"
kits = urlopen(url)
response  = kits.read()
print response

# Make a GET request here and assign the result to kittens:

#kittens = requests.get("http://placekitten.com/")
#print kittens.text[559:1000]