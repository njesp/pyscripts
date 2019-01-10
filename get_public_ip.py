import json
import requests
import datetime
ip = json.loads(requests.get('https://api.ipify.org?format=json').text)['ip']
with open('/home/pi/ip.txt', 'a') as myfile:
    myfile.write(datetime.datetime.today().strftime(
        '%Y-%m-%d;%H:%M:%S') + ';' + ip + '\n')
#cat ip.txt | cut -d ';' -f3 | uniq

