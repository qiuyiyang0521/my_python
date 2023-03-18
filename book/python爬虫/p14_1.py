from turtle import width
from urllib import response
import urllib.request
req = urllib.request.Request('https://placekitten.com/g/1920/1028')
response = urllib.request.urlopen(req)
cat_img = response.read()

with open('E:\\GitHub\\my_python\\book\\python爬虫\\资源\\cat_g_1920_1028.jpg', 'wb') as f:
    f.write(cat_img)
