import urllib.request as r
import headers

url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20'

request = r.Request(url,headers=headers.HEADERS)
response = r.urlopen(request)
content = response.read().decode('utf-8')

with open('./file/douban.json','w',encoding='utf-8') as file:
    file.write(content)
