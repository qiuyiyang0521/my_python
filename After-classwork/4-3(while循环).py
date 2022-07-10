# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-05 15:24:34
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:03:55
import os


os.system("pause")

i =1
sum =0
num = int(input('你要计算前几项的和？'))
while i <= num:
    sum += i
    i += 1

print("前", num,"项的和是：", sum)


