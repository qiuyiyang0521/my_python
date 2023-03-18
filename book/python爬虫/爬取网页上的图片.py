from urllib.request import urlretrieve
import requests
from lxml import etree



def download_thread(*, filename, url, num):
    print(url)
    print(f'开始下载第{num}张')
    urlretrieve(url, filename)
    print(f'第{num}张下载完成')


def main():
    

main()
