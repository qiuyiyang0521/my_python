import headers
import urllib.request as r
import urllib.error as e

url = 'https://csdnnews.blg.csdn.net/article/details/1286399271'
try:
    request = r.Request(url, headers=headers.HEADERS)
    response = r.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except e.HTTPError:
    print('系统正在升级。。。')

except e.URLError:
    print('我都说了系统正在升级。。。')
