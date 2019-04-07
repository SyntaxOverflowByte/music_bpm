"""
Beautiful Soup
"""

import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlencode, urljoin
#from urllib.parse import urljoin

args_search = True
args_artist = False
args_song = False

api_key = "4a45338f3b72c92981ea4c26c94ebf61"
web_base = "https://api.getsongbpm.com"

if args_search:
	web_search = urljoin(web_base, '/search/')
elif args_artist:
	web_search = urljoin(web_base, '/artist/')
elif args_song:
	web_search = urljoin(web_base, '/song/')


def getArtistID(artist_name):
	u = {
		'type' : 'artist',
		'api_key' : api_key,
		'lookup' : artist_name
	}
	req = requests.get(urljoin(web_search, '?' + urlencode(u)))
	if req.status_code == 200:
		return req.json()['search'][0]['id']

def getSongID(song_name):
	u = {
		'type' : 'song',
		'api_key' : api_key,
		'lookup' : artist_name
	}
	req = requests.get(urljoin(web_search, '?' + urlencode(u)))
	#if req.status_code