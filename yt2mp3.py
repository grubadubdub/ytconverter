import requests
from bs4 import BeautifulSoup as leSoup

# find source script scramble
# get hash thing from scramble
# send get to check.php
# 	- callback:
# 	- f: mp3
# 	- v: video
#   - k: unscramble
# 	- _:

data = requests.get('https://ytmp3.cc/')
soup = leSoup(data.text, 'html.parser')

scripts = soup.findAll('script')
for script in scripts:
	print(script['src'])

data = {
	'v':,
	'f': 'mp3',
	'k':,
}



def unscramble(h):
	

print(data.content)