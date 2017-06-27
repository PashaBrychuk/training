# images.py  https://www.youtube.com/watch?v=8vwoc0n6Isc


import requests
print requests

def download_one_file(url):

	r = requests.get(url, stream = True)
	print r
	with open("1.jpg", "wb") as f:
		for chunk in r.iter_content():
			f.write(chunk)


url = "http://www.hdwallpapers.in/thumbs/2016/life_game_win-t2.jpg"


#download_one_file(url)
urls = ["http://www.hdwallpapers.in/walls/life_game_win-wide.jpg", "http://www.hdwallpapers.in/thumbs/2013/be_happy=t2.jpg"]

def download_list_of_files():