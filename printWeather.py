#coding:utf-8
#!/usr/bin/python
import requests
KEY = 'YRZU3XTGYJ'
CITY = 'Zhuhai'
URL = 'https://api.thinkpage.cn/v2/weather/now.json?city=%s&language=en&unit=c&key=%s'%(CITY.lower(), KEY)

try:
    x = requests.get(URL).json()
    print(x['weather'][0]['now']['text'])
except:
    pass
