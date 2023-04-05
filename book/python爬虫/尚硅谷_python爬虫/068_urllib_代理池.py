# 找不到能用的ip,随便玩玩
proxies_pool = [{'http': 'http://14.139.173.182:80'},
                {'http': 'http://139.180.137.52:80'},
                {'http': 'http://51.81.87.123:80'},
                {'http': 'http://185.174.111.25:41002'}]
import urllib.request as r
from headers import HEADERS
import random

url = 'https://www.baidu.com'
request = r.Request(url,headers=HEADERS)
while True:
    try:
        response = r.urlopen(request)
        print(response.status)
    except Exception as e:
        print(e)