# images.py  https://www.youtube.com/watch?v=8vwoc0n6Isc
import requests
print requests
url = "http://www.hdwallpapers.in/thumbs/2016/life_game_win-t2.jpg"
r = requests.get(url, stream = True)
print r
with open("1.jpg", "wb") as f:
	for chunk in r.iter_content():
		f.write(chunk)