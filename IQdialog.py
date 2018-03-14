"""import requests
from urllib2 import urlopen

response =("https://iq-uat.wds.co/api/dialog?json={%22version%22:6,%22evidence%22:[{%22source%22:%22CUSTOMER%22,%22algorithms%22:[],%22ordinal%22:1,%22evidence%22:{%22translations%22:{%22en%22:%22unable%20to%20connect%20to%20wifi%22},%22type%22:%22STATEMENT%22}}],%22context%22:{%22contentGroup%22:%22638%22},%22metadata%22:{%22algorithms%22:[%22aos%22],%22algorithmParameters%22:{%22map%22:{},%22classInstantiator%22:{}},%22diagnosticsRequired%22:{},%22locale%22:%22en%22,%22sessionId%22:%2201-cb539f8a-664f-4889-bcb6-3192a3fc5e72%22,%22tracking%22:true,%22relevantEvidence%22:false,%22greedyFixFetch%22:true,%22retrieveFixes%22:true,%22aosGiveUpEarly%22:true}}")
z = response.read()

print z

"""

"""
import requests
response = requests.get("https://iq-uat.wds.co/api/dialog?json={%22version%22:6,%22evidence%22:[{%22source%22:%22CUSTOMER%22,%22algorithms%22:[],%22ordinal%22:1,%22evidence%22:{%22translations%22:{%22en%22:%22unable%20to%20connect%20to%20wifi%22},%22type%22:%22STATEMENT%22}}],%22context%22:{%22contentGroup%22:%22638%22},%22metadata%22:{%22algorithms%22:[%22aos%22],%22algorithmParameters%22:{%22map%22:{},%22classInstantiator%22:{}},%22diagnosticsRequired%22:{},%22locale%22:%22en%22,%22sessionId%22:%2201-cb539f8a-664f-4889-bcb6-3192a3fc5e72%22,%22tracking%22:true,%22relevantEvidence%22:false,%22greedyFixFetch%22:true,%22retrieveFixes%22:true,%22aosGiveUpEarly%22:true}}")
print response.read"""

import urllib
import json
import requests
site = "https://iq-uat.wds.co/api/dialog?json={%22version%22:6,%22evidence%22:[{%22source%22:%22CUSTOMER%22,%22algorithms%22:[],%22ordinal%22:1,%22evidence%22:{%22translations%22:{%22en%22:%22unable%20to%20connect%20to%20wifi%22},%22type%22:%22STATEMENT%22}}],%22context%22:{%22contentGroup%22:%22638%22},%22metadata%22:{%22algorithms%22:[%22aos%22],%22algorithmParameters%22:{%22map%22:{},%22classInstantiator%22:{}},%22diagnosticsRequired%22:{},%22locale%22:%22en%22,%22sessionId%22:%2201-cb539f8a-664f-4889-bcb6-3192a3fc5e72%22,%22tracking%22:true,%22relevantEvidence%22:false,%22greedyFixFetch%22:true,%22retrieveFixes%22:true,%22aosGiveUpEarly%22:true}}"
content = urllib.urlopen(site)
z = content.read()
#print z

print z
print type(z)
d = json.loads(z)
print d
print type(d)