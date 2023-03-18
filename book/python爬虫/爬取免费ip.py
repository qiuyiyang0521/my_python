from lxml import etree
import requests
from headers import HEADERS


def get_ip(url):
    response = requests.get(url, headers=HEADERS)
    print(response.status_code)
    # response.encoding = 'utf-8'
    # if response.status_code == 200:
    #     html = etree(response.text)
    #     html.xpath('//table[@class="table table-bordered table-striped]')
    #     print(html)


if __name__ == '__main__':
    for page in range(10):
        url = f'https://www.kuaidaili.com/free/inha/{page + 1}/'
        get_ip(url)

