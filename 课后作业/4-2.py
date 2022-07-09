# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-05 15:24:34
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:03:54
import os


os.system("pause")


import turtle
turtle.bgcolor("black")
t=turtle.Pen()
t.speed(0)
num = int(turtle.numinput("圆的个数","请输入绘制的圆的数量？",6,3,30))
for x in range(num):
    t.pencolor("red")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(50)
    t.left(360 // num)
    

print("绘制结束")
