# parse site using python   https://www.youtube.com/watch?v=KPXPr-KS-qk&t=441s
import urllib2
import requests
from bs4 import BeautifulSoup
def get_html(url):
	response = urllib2.urlopen(url)
	return response.read()
#print get_html("https://auto.ria.com/legkovie/renault/laguna/")


"""r = urllib2.urlopen("https://auto.ria.com/legkovie/renault/laguna/")
print r.read()
z = r.read()

"""
def parse(html):
	soup = BeautifulSoup(html, "html.parser")
	table = soup.find("table" , class_ ="standart-view")
	print table.prettify()
print parse("https://auto.ria.com/legkovie/renault/laguna/")
