import urllib.request
from headers import HEADERS
from bs4 import BeautifulSoup

url = 'https://www.baidu.com'

request = urllib.request.Request(url=url, headers=HEADERS)
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
content = BeautifulSoup(content).prettify()
print(content)
