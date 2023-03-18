import urllib.request
import urllib.parse
import headers

name = urllib.parse.quote('周杰伦')
url = f'https://www.baidu.com/s?wd={name}'
_headers = headers.HEADERS

request = urllib.request.Request(url,headers=_headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
