import requests
from bs4 import BeautifulSoup
import headers
from urllib.request import urlretrieve

url = 'https://www.starbucks.com.cn/menu/'
response = requests.get(url,headers=headers.HEADERS)
if response.status_code == 200:
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    name_list = soup.select('ul[class="grid padded-3 product"] strong')
    for name in name_list:
        print(name.string)