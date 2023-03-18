import urllib.request as r
from headers import HEADERS

url = 'http://www.baidu.com/s?wd=ip'
proxies = {
    'http': 'http://185.218.125.70:80',
    'https': 'https://185.218.125.70:80'
}

request = r.Request(url, headers=HEADERS)
handler = r.ProxyHandler(proxies=proxies)
openr = r.build_opener(handler)
response = openr.open(request)
content = response.read().decode('utf-8')

with open('./file/daili.html','w', encoding='utf-8') as file:
    file.write(content)
