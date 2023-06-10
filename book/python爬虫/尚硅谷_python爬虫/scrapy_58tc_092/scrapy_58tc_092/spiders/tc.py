import scrapy
from lxml import etree


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["cn.58.com"]
    start_urls = ["https://cn.58.com/sou/?key=前端开发&classpolicy=uuid_b4d75428d0554c22b59a142ad39586d7,classify_A&search_uuid=b4d75428d0554c22b59a142ad39586d7"]

    def parse(self, response):
        content = response.text
        print('=' * 250)
        print(etree.HTML(response.text).xpath('//title/string'))
        print('=' * 250)
