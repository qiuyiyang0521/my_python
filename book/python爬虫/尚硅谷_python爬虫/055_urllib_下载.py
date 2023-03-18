import urllib.request

headers={
        'User-Agent':
        ' Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/108.0.0.0 Safari/537.36 \
        Edg/108.0.1462.76'}
# 下载网页
url_page = 'https://www.baidu.com'
urllib.request.urlretrieve(
    url_page,
    '../资源/百度主页.html'
    )
# 视频

# 图片
