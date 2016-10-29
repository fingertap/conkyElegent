KEY = 'YRZU3XTGYJ'
import requests
details = requests.get('http://ipinfo.io/json').json()
CITY=details['city']
COUNTRY=details['country']
LATITUDE=details['loc'].split(',')[0]
LONGITUDE=details['loc'].split(',')[1]
