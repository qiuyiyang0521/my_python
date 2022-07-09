# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-09 11:33:01
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 11:58:33
import os
import turtle
answer = str(input("你想要绘制一个螺旋线吗？(y/n)"))
if answer == "y":
	for x in range(100):
		t.forward(x * 2)
		t.right(360 / 4 + 1)
	t.done()
else:
	print("感谢你使用这个程序！")

os.system("pause")
