# parse site using python   https://www.youtube.com/watch?v=KPXPr-KS-qk&t=441s
#import urllib2
import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	#print r.text
	return r.text

def get_total_pages_number(html):
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find('div', class_= 'pagination-pages').find_all('a', class_= 'pagination-page')[-1]#.get('href')

	print pages
	pages = soup.find('div', class_= 'pagination-pages').find_all('a', class_= 'pagination-page')[-1].get('href')
	print pages

	total_pages = pages.split("=")[1]
	total_pages = total_pages.split("&")[0]
	print type(total_pages)
	print total_pages#print get_html("https://auto.ria.com/legkovie/renault/laguna/")
	return int(total_pages)


def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	ads = soup.find
			
def main():
	url = "http://www.avito.ru/moskva/telefony?p=1&q=htc"
	base_url = "http://www.avito.ru/moskva/telefony?"
	page_part = "p="
	query_part = "&q=htc"
	total_pages =  get_total_pages_number(get_html(url))
	for i in range(1, 3):
		url_gen = base_url+page_part+str(i)+query_part
		#print url_gen
		html  = get_html(url_gen)
		get_page_data(html)


if __name__ == '__main__':
	main()


#print get_total_pages_number(get_html("http://www.avito.ru/moskva/telefony?p=1&q=htc"))
