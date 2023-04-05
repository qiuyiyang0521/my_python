from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# 添加配置，程序运行完后不关闭浏览器
# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach',True)

s = Service('./chromedriver.exe')
# browser = webdriver.Chrome(service=s,options=option)
browser = webdriver.Chrome(service=s)

url = 'https://www.jd.com'
browser.get(url)

content = browser.page_source
print(content)