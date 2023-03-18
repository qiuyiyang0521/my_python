import requests
from bs4 import BeautifulSoup
from lxml import etree

# q = input('搜索:')
q = '鸡你太美'
url = f'https://cn.bing.com/search?q={q}'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
content = BeautifulSoup(response.text,'lxml').prettify()
soup = BeautifulSoup(content,'lxml')
request_contents = soup.find(name='ol',id='b_results')
request_contents_list = request_contents.find_all(name='li',class_='b_algo')
for x in request_contents_list:
    print(x)
    
