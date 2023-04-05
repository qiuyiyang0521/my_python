from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_experimental_option('detach',True)

service = Service('./chromedriver.exe')
chrome = Chrome(service=service,options=option)

url = 'https://www.baidu.com'
chrome.get(url)

chrome.implicitly_wait(2)

input = chrome.find_element(By.ID,'kw')
input.send_keys('周杰伦')

chrome.implicitly_wait(2)

button = chrome.find_element(By.ID,'su')
button.click()
