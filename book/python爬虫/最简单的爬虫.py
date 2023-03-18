# -*-coding:utf-8-*-
import requests
import bs4
import re


def main():
    url = input("网址(必填)：")
    name = input('文件名(不带后缀)')
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'
    }
    proxies = {
        'http': '127.0.0.1:1080', 'https': '127.0.0.01:1080'
    }
    res = requests.get(url, headers=headers)
    url_text = 'E:\\GitHub\\my_python\\book\\python爬虫\\资源' + '\\' + name + '.txt'
    with open(url_text, 'w', encoding='utf-8') as f:
        f.write(res.text)
    print('程序结束')


if __name__ == '__main__':
    main()
