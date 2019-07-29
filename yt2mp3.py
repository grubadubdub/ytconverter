import sys
import urllib.request
import shutil
from selenium import webdriver

# - navigate to page and run ajax
# - get ajax response
# - download file from response

vlink = sys.argv[1][32:]
o = ['.oeaa.cc', 'cco', 'aea', 'oea', 'aoa', 'cee', 'coe', 'oca', 'caa', 'eae', 'oce', 'eao', 'oco', 'eoo', 'coc', 'aco', 'aae', 'coo', 'ooa', 'cao', 'aoe', 'oeo', 'ece', 'eeo', 'oac', 'eec', 'oec', 'eoe', 'eaa', 'eoa', 'ecc', 'cec', 'ceo', 'aee', 'cae', 'eoc', 'oae', 'cce', 'ooe', 'aao', 'aec', 'cca', 'oaa']

url = 'https://ytmp3.cc/'

# myscript = os.getcwd() + '\\getsongs.js'
# fp = open(myscript, 'r')

options = webdriver.FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get(url)

js = 'var l = [\'' + vlink + '\'];' + 'for (var i=0;i<l.length;i++) {$.ajax({url:"https://a.oeaa.cc/check.php", data:{v:l[i],f:\'mp3\',k:\'heu6q64eh6pf4moiBELtxuoqvvtZ\'}, dataType:"jsonp", success: arguments[0]});}'

# wait for ajax items to load
try:
    result = driver.execute_async_script(js)
    sid   = result['sid']
    hashc = result['hash']
    title = result['title']
except KeyError:
    print(result)
    print('ERROR')
finally:
    driver.quit()

song = 'https://' + o[int(sid)] + o[0] + '/' + hashc + '/' + vlink

# download the file from `url` and save it locally under `file_name`
# https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3

with urllib.request.urlopen(song) as response, open(title+'.mp3', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

