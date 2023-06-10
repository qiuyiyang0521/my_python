from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()
option.add_experimental_option('detach', True)

service = Service('./chromedriver.exe')
chrome = Chrome(service=service, options=option)

url = 'https://www.baidu.com'
chrome.get(url)

sleep(2)

input = chrome.find_element(By.ID, 'kw')
input.send_keys('周杰伦')

sleep(2)

button = chrome.find_element(By.ID, 'su')
button.click()

sleep(2)

js_button = 'document.documentElement.scrollTop=100000'
chrome.execute_script(js_button)

sleep(2)

next = chrome.find_element(By.XPATH, '//a[@class="n"]')
next.click()

sleep(2)

chrome.back()

sleep(2)

chrome.forward()

sleep(3)

chrome.quit()
