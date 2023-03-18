from urllib import request as r
from headers import HEADERS
from lxml import etree

url = 'https://www.baidu.com'
request = r.Request(url,headers=HEADERS)
response = r.urlopen(request)
content = response.read().decode('utf-8')
tree = etree.HTML(content)
result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)
