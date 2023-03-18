import urllib.request
import urllib.parse
import json
import headers

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw':'spider'
}
# post请求的参数必须进行编码
data = bytes(urllib.parse.urlencode(data),encoding='utf-8')

request = urllib.request.Request(url=url,data=data,headers=headers.HEADERS)
resp = urllib.request.urlopen(request)
content = resp.read().decode('utf-8')
obg = json.loads(content)
print(obg)
