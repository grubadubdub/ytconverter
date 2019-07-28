import os
import urllib.request
import shutil
from selenium import webdriver

o = ['.oeaa.cc', 'cco', 'aea', 'oea', 'aoa', 'cee', 'coe', 'oca', 'caa', 'eae', 'oce', 'eao', 'oco', 'eoo', 'coc', 'aco', 'aae', 'coo', 'ooa', 'cao', 'aoe', 'oeo', 'ece', 'eeo', 'oac', 'eec', 'oec', 'eoe', 'eaa', 'eoa', 'ecc', 'cec', 'ceo', 'aee', 'cae', 'eoc', 'oae', 'cce', 'ooe', 'aao', 'aec', 'cca', 'oaa']

url = 'https://ytmp3.cc/'

myscript = os.getcwd() + '\\getsongs.js'
fp = open(myscript, 'r')

options = webdriver.FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get(url)

#wait for ajax items to load
result = driver.execute_async_script(fp.read())
fp.close()
sid   = result['sid']
hashc = result['hash']
title = result['title']

song = 'https://' + o[int(sid)] + o[0] + '/' + hashc + '/' + 'heu6q64eh6pf4moiBELtxuoqvvtZ'
# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(song) as response, open(title+'.mp3', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

