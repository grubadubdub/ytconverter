import sys
import urllib.request
import shutil
from selenium import webdriver

# - ask for links before inputting all in js?
# - navigate to page
# - get scramble from jquery for get request
#       -- already in js
#       -- use unscrambled scramble to run ajax
# - get hash from response
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

while (run):

js = 'var l = [\''+ vlink +'\']'+ '''
function p(t){
    for(var e=0, r=0, s=""; r<t.length; r++) {
        if(e=t.charCodeAt(r), 64<e && e<91) 
            e = e == 65 ? 90 : e-1;
        else if (96<e && e<123)
            e = e == 122 ? 97 : e+1;
        else if(47<e && e<53)
            switch(e) {
                case 48:
                    e=57;
                    break;
                case 49:
                    e=56;
                    break;
                case 50:
                    e=55;
                    break;
                case 51:
                    e=54;
                    break;
                case 52:
                    e=53;
            }
        else 
            52<e && e<58 ? e=Math.round(h(e.toString())/2).toString().charCodeAt(0):e==45&&(e=95);
        s+=String.fromCharCode(e)
    }
    return s
}

for(var i=0, r='';i<$("script").length;i++)
    if(r=/ytmp3\.js\?[a-z]{1}\=[a-zA-Z0-9\-\_]{16,40}/.exec($("script")[i].src)) {
        r=p(r.toString().slice(11));
        break
    }
for (var i=0;i<l.length;i++) {
    $.ajax({
        url:"https://a.oeaa.cc/check.php", 
        data: {
            v:l,
            f:'mp3',
            k:r
            }, 
        dataType:"jsonp", 
        success: arguments[0]
    });
}
'''

# print(js)

# wait for ajax items to load
try:
    result = driver.execute_async_script(js)
    sid   = result['sid']
    hashc = result['hash']
    title = result['title']
except KeyError:
    print('Error in fetching song')
    print(result)
finally:
    driver.quit()

song = 'https://' + o[int(sid)] + o[0] + '/' + hashc + '/' + vlink

# download the file from `url` and save it locally under `file_name`
# https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3

with urllib.request.urlopen(song) as response, open(title+'.mp3', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

