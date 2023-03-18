import urllib.parse
import urllib.request
import headers

data = {
    'wd': '周杰伦',
    'sex': '男'
}
base_url = 'https://www.baidu.com/s?'

data = urllib.parse.urlencode(data)
url = base_url + data

request = urllib.request.Request(url=url,headers=headers.HEADERS)
resp = urllib.request.urlopen(request)
content = resp.read().decode('utf-8')

with open("baidu.html",'w',encoding='utf-8') as file:
    file.write(content)
