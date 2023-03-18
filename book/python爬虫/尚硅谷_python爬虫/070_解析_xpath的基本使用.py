from lxml import etree

html = etree.parse('070_解析_xpath的基本使用.html')
print(html.xpath('//ul/li[@id="a1"]/text()'))
print(html.xpath('//ul/li[contains(@id,"a")]/text()'))
# 写太多没意思，别的书里有
