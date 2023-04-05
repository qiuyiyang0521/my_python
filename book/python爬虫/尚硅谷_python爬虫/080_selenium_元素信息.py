from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver.exe')
chrome = Chrome(service=service)

url = 'https://www.baidu.com'
chrome.get(url)

input = chrome.find_element(By.ID,'su')
print(input.get_attribute('class'))
print(input.tag_name)
print(input.text)
print(input.get_attribute('value'))
