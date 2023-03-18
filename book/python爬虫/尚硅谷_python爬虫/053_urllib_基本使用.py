# 获取百度首页源代码

import urllib.request

url = 'https://www.baidu.com'

# 向服务器发送请求
response = urllib.request.urlopen(url)

# 获取响应的页面源吗
content = response.read().decode('utf-8')

print(content)
