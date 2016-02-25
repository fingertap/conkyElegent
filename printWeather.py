#coding:utf-8
#!/usr/bin/python
import requests
from config import *
URL = 'https://api.thinkpage.cn/v2/weather/now.json?city=%s&language=en&unit=c&key=%s'%(CITY.lower(), KEY)

try:
    x = requests.get(URL, timeout=5).json()
    print(x['weather'][0]['now']['text'])
except:
    pass
