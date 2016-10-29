import re
import json
from urllib2 import urlopen

data = str(urlopen('http://checkip.dyndns.com/').read())
IP = re.compile(r'(\d+.\d+.\d+.\d+)').search(data).group(1)
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)

org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('Your IP detail\n')
print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,reg,ctry,city,IP))
