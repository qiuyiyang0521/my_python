# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-09 16:17:47
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 16:36:17

import time

num = int(input("请输入一个整数"))
time.sleep(0.5)
if num % 2 == 0:
	print("它是一个偶数")
else:
	print("它是一个奇数")

time.sleep(0.5)
print("运行结束")
