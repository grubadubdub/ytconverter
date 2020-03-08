import spotipy
import spotipy.util as util
import json
from json.decoder import JSONDecodeError
import os

# add checkbox for manual, auto spotify search



# items -> album   -> images
# 			     -> name
# 			     -> total tracks
# 	  -> artists -> name

username = '31jbzyaxatd7q37tat6urb5xeuve'


def search(query):
	print(query)

	# REGEX CLEANUP

	# try:
	# 	token = util.prompt_for_user_token(username)
	# except:
	# 	os.remove(f".cache-{username}")
	# 	token = util.prompt_for_user_token(username)
	# 	# print('not working')
	# 	# return

	# # create spotifyOBject
	# spotifyObject = spotipy.Spotify(auth=token)


	# # spotify = spotipy.Spotify()
	# results = spotifyObject.search(q=query, type='track')
	# print(json.dumps(results, indent=4))

search('KATIE - Thinkin Bout You ดาหสาหก')