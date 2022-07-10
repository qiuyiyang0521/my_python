# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-05 15:24:34
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:03:57
import os


os.system("pause")

#画num个圆
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
num = int(turtle.numinput("圆的个数","请输入你要绘制的圆的个数",6,3,30))
for x in range(num):
    t.pencolor("red")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(50)
    
    t.left(360//num)


print("运行结束") #这句话不再循环的控制范围内
