import requests
from bs4 import BeautifulSoup as leSoup

# find source script scramble
# get hash thing from scramble
# send get to check.php
# 	- callback: from network??
# 	- f: unscramble
# 	- v: video
# 	- _: in scramble

data = requests.get('https://ytmp3.cc/')
soup = leSoup(data.text, 'html.parser')

scripts = soup.findAll('script')
for script in scripts:
	print(script['src'])

print(data.content)