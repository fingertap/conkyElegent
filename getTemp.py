#coding:utf-8
#!/usr/bin/python
import requests
from config import *
URL = 'https://api.thinkpage.cn/v2/weather/now.json?city=%s&language=en&unit=c&key=%s'%(CITY.lower(), KEY)

try:
    x = requests.get(URL, timeout=5).json()
    cur_temp = x['weather'][0]['now']['temperature']
    print(cur_temp, end="")
    if len(cur_temp) < 2:
        print(' ', end="")
    cur_weather_code = x['weather'][0]['now']['code']
    import shutil
    target = '/home/han/.conky/weather/dummy.png'
    origin = '/home/han/.conky/weather/%s.png'%cur_weather_code
    shutil.copyfile(origin, target)
except:
    print('NA')
    import shutil
    target = '/home/han/.conky/weather/dummy.png'
    origin = '/home/han/.conky/weather/na.png'
    shutil.copyfile(origin, target)
