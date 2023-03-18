import urllib.request as r
from headers import *
url = 'https://www.gulixueyuan.com/course/455/task/20264/show'
HEADERS += {'cookie': 'REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOXphbWMzY1dvM04zcEFaV1IxYzI5b2J5NXVaWFE9OjE3MDY1ODY1NDI6OTc4NjM5M2IzYzFjOTZlZjJhZjhhOWRmNGZmZmJiNGNkMWRkYTk2MzRjNjI3YTU4MDMyY2EzYWNmMDY3Njk5Mg==; PHPSESSID=bhho69bkrmpqcfomkutsst19m7; online-uuid=7A44F9D9-D3CC-142D-00FD-EE5FF7FB0183'
            }
request = r.Request(url, headers=HEADERS)
response = r.urlopen(request)
content = response.read().decode('utf-8')

with open('./file/shangguigu.html', 'w', encoding='utf-8') as file:
    file.write(content)
