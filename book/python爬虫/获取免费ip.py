import requests
from headers import HEADERS
from lxml import etree

for x in range(10):
    url = 'http://www.66ip.cn/{i}.html'.format(i=x)
    response = requests.get(url,headers=HEADERS)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        content = response.text
        tree = etree.HTML(content)
        td = tree.xpath('/html/body/div[4]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]')
        print(td)
