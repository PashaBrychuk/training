#bs.p based on yhttps://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests


def get_html(url):
	r = requests.get(url)
	s = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
	"""with open('somefile.txt', 'w') as f:
		f.write(s)"""
	return r.text

def get_total_pages(html):
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find_all('title')
	return pages

url = "https://auto.ria.com/search/?year[0].gte=2006&year[0].lte=2008&categories.main.id=1&brand.id[0]=62&model.id[0]=3185&sort[0].price.order=asc&custom.not=1&page=0&size=20"
#url = "https://www.avito.ru/moskva/telefony?p=1&q=htc"
print get_total_pages(get_html(url))

