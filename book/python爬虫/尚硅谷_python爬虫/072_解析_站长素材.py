import urllib.request as r
from lxml import etree
from headers import HEADERS


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/fengjing.html'
    else:
        url = f'https://sc.chinaz.com/tupian/fengjing_{str(page)}.html'
    request = r.Request(url=url, headers=HEADERS)
    return request


def get_content(url):
    response = r.urlopen(url=url)
    content = response.read().decode('utf-8')
    return content

def get_result(url,num):
    print(f'下载第{num}张。')
    


if __name__ == '__main__':
    start_page = int(input('起始页码:'))
    end_page = int(input('结束页码:'))
    for page in range(start_page, end_page + 1):
        request = create_request()
        content = get_content(request)
