#coding:utf-8
#!/usr/bin/python
import requests
KEY = 'YRZU3XTGYJ'
CITY = 'Zhuhai'
# CITY = 'Chengdu'
URL = 'https://api.thinkpage.cn/v2/weather/now.json?city=%s&language=en&unit=c&key=%s'%(CITY.lower(), KEY)

try:
    x = requests.get(URL).json()
    print(x['weather'][0]['now']['temperature'])
    # cur_weather = x['weather'][0]['now']['text']
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
