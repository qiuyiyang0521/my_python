# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-09 16:04:42
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 16:15:09

'''
如果身高超过140cm应该买成人票，
如果身高在120cm到140cm之间买儿童票，
如果身高低于120cm不用买票。
'''
import time

height = int(input("你的身高是多少厘米？"))
time.sleep(1)
if height > 140:
	print("你应该买成人票。")
elif 120 <= height <= 140:
	print("你应该买儿童票。")
else:
	print("你不用买票。")
time.sleep(1)
print("感谢你使用这个程序！")
