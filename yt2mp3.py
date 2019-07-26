import requests
from math import ceil
from bs4 import BeautifulSoup as leSoup

# find source script scramble  /
# get hash thing from scramble /
# send get to check.php
# 	- callback:
# 	- f: mp3
# 	- v: video
#   - k: unscramble
# 	- _:

# // connect to url and find script src

data = requests.get('https://ytmp3.cc/')
soup = leSoup(data.text, 'html.parser')

scripts = soup.findAll('script')
for script in scripts:
	if 'ytmp3.js?' in script['src']:
		ind = script['src'].find('&')
		k = script['src'][15:ind]
		break


# // get k value from script src

def cases(c):
	switcher = {
		48: 57,
		49: 56,
		50: 55,
		51: 54,
		52: 53
	}
	return switcher.get(c, c)

def unscramble(h):
	ret = ""
	for letter in h:
		code = ord(letter)
		if 64 < code and code < 91:
			code = 90 if code == 65 else code-1
		elif 96 < code and code < 123:
			code = 97 if code == 122 else code+1
		elif 47 < code and code < 53:
			code = code = cases(code)
		elif 52 < code and code < 58:
			code = ord(str(ceil(int(letter)/2)))
		else:
			code = 95 if code == 45 else code
		ret += chr(code)
	return ret


# // prep for request
data = {
	'v': 'asdf',
	'f': 'mp3',
	'k': unscramble(k),
}