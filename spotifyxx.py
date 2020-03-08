import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# SPOTIFY PLAN #
# - assume .mp3 file ready
# - file will probably have some metadata info
# - ARTIST - TRACK ... (Official ... )
find 



# get username from terminal
# username = sys.argv[1]
username = '31jbzyaxatd7q37tat6urb5xeuve'

# user ID: 31jbzyaxatd7q37tat6urb5xeuve

# erase cache and prompt for permission
try:
	token = util.prompt_for_user_token(username)
except:
	os.remove(f".cache-{username}")
	token = util.prompt_for_user_token(username)

# create spotifyOBject
spotifyObject = spotipy.Spotify(auth=token)


# set SPOTIPY_CLIENT_ID=ca1262827006440dbd4c0371af08d13e
# set SPOTIPY_CLIENT_SECRET=aa7da1e3afdd4f2cb416f1d730a75c64
# set SPOTIPY_REDIRECT_URI=http://google.com/

user = spotifyObject.current_user()
print(json.dumps(user, sort_keys=True, indent=4))


while True:
	print()
	print('>>> Welcome to Spotipy!')
	print()
	print('0 - Search for an artist')
	print('1 - Exit')
	choice = input('Your choice: ')

	if choice == "0":
		print('0')
		searchQuery = input("OK, what's the artist name? ")
		print()

		searchResults = spotifyObject.search(searchQuery,1,0,'artist')
		print("You're searching for " + searchQuery)
		print(json.dumps(searchResults, sort_keys=True, indent=4))

	else:
		break




# import requests
# from math import ceil
# from bs4 import BeautifulSoup as leSoup
# import requests.packages.urllib3.connectionpool as httplib
# import logging
# import json

# # find source script scramble  /
# # get hash thing from scramble /
# # send get to check.php
# #     - callback:
# #     - f: mp3
# #     - v: video
# #   - k: unscramble
# #     - _:


# httplib.HTTPConnection.debuglevel = 1
# # You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig(
)# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True


# def cases(c):
#   switcher = {
#       48: 57,
#       49: 56,
#       50: 55,
#       51: 54,
#       52: 53
#   }
#   return switcher.get(c, c)

# def unscramble(h):
#   ret = ""
#   for letter in h:
#       code = ord(letter)
#       if 64 < code and code < 91:
#           code = 90 if code == 65 else code-1
#       elif 96 < code and code < 123:
#           code = 97 if code == 122 else code+1
#       elif 47 < code and code < 53:
#           code = cases(code)
#       elif 52 < code and code < 58:
#           code = ord(str(ceil(int(letter)/2)))
#       else:
#           code = 95 if code == 45 else code
#       ret += chr(code)
#   return ret


# # // connect to url in a session and find script src

# session = requests.Session()
# data = session.get('https://ytmp3.cc/')
# # print(session.cookies.get_dict())
# cookies = session.cookies.get_dict()['PHPSESSID']

# soup = leSoup(data.text, 'html.parser')

# scripts = soup.findAll('script')
# for script in scripts:
#   if 'ytmp3.js?' in script['src']:
#       ind = script['src'].find('&')
#       k = script['src'][15:ind]
#       break

# # // params for request
# data = {
#   'v': 'Ryg62SUcYKE',
#   'f': 'mp3',
#   'k': unscramble(k),
# }

# headers = {'content-type': 'application/json'}

# # // send get to check.php
# r = session.get('https://ytmp3.cc/check.php', params=data, headers=headers)
# # r = session.get('https://httpbin.org/get', params=data)
# print(r.get_json())
