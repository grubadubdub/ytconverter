import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError





# get username from terminal
username = sys.argv[1]

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
