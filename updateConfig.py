from key import *
if __name__ == '__main__':
    CITY = 'NA'
    COUNTRY = 'NA'
    TARGET_FIG = '/home/han/.conky/weather/na.png'
    TEMPERATURE = 'NA'
    WEATHER = 'NA'
    import requests
    try:
        ip = requests.get('http://ipinfo.io/json').json()['ip']
        url = 'https://api.thinkpage.cn/v3/location/search.json?key=%s&q=%s&language=en'%(KEY, ip)
        details = requests.get(url).json()['results'][0]
        CITY_ID = details['id']
        CITY = details['name']
        COUNTRY = details['country']
    except:
        pass
    try:
        # try get the city name with the location information
        URL = 'https://api.thinkpage.cn/v2/weather/now.json?city=%s&language=en&unit=c&key=%s'%(CITY_ID, KEY)
        x = requests.get(URL, timeout=5).json()
        TEMPERATURE = x['weather'][0]['now']['temperature']
        WEATHER = x['weather'][0]['now']['text']
        cur_weather_code = x['weather'][0]['now']['code']
        TARGET_FIG = '/home/han/.conky/weather/%s.png'%cur_weather_code
    except:
        pass
        #print('Weather fetch fail')
    try:
        f = open('/home/han/.conky/CONFIGS.py', 'w')
        f.write('CITY=\'%s\'\n'%CITY)
        f.write('COUNTRY=\'%s\'\n'%COUNTRY)
        f.write('TARGET_FIG=\'%s\'\n'%TARGET_FIG)
        f.write('TEMPERATURE=\'%s\'\n'%TEMPERATURE)
        f.write('WEATHER=\'%s\'\n'%WEATHER)
        f.close()
    except:
        pass

