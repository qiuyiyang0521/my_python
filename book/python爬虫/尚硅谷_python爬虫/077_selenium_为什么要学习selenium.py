from urllib import request as r
from headers import HEADERS

url='https://www.jd.com'
request = r.Request(url,headers=HEADERS)
response = r.urlopen(request)
content = response.read().decode('utf-8')
print(content)