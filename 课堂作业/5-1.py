# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date:   2022-07-09 10:19:54
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:08:19
import turtle as t
import os
answer = str(input("你想要绘制一个圆吗？(y/n)"))
if answer == "y":
	t.circle(100)
	t.done()
else:
	print("感谢你使用这个程序！")

os.system("pause")
