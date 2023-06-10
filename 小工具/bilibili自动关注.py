from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from time import sleep

with open('./bilibili_follow.txt', 'r', encoding='utf-8') as fp:
    content = fp.read()
    follow = content.split('\n')

service = Service('./chromedriver.exe')
chorme = Chrome(service=service)

for x in follow:
    chorme.get(f'https://search.bilibili.com/all?keyword={x}&from_source=webtop_search')
    sleep(5)
