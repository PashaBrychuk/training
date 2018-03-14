#parse_site.py
import requests
from BeautifulSoup import BeautifulSoup
html = requests.get('http://baskino.club/new').text
print type(html)
soup = BeautifulSoup(html)
print type(soup)
print soup.findAll('a')
