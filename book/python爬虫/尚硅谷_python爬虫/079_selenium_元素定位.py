from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')
chrome = Chrome(service=service)

url = 'https://www.baidu.com'
chrome.get(url)

# button = chrome.find_element(By.ID,'su')
# print(button)

# button = chrome.find_element(By.NAME,'wd')
# print(button)

# button = chrome.find_elements(By.XPATH,'//input[@id="su"]')[0]
# print(button)

# button = chrome.find_elements(By.TAG_NAME,'input')
# print(button)

# button = chrome.find_element(By.CSS_SELECTOR,'#su')
# print(button)

# button = chrome.find_element(By.LINK_TEXT,'直播')
# print(button)