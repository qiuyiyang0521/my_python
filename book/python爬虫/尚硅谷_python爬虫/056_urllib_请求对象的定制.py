import urllib.request

url = 'https://www.baidu.com'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
request = urllib.request.Request(url=url,headers=headers)
resp = urllib.request.urlopen(request)
content = resp.read().decode('utf-8')
print(content)
