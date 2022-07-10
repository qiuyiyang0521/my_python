# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-08 15:35:16
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:03:56
import os


os.system("pause")

import turtle as t
t = input("wjfdf")
t.penup()
sides = int(t.numinput('边数','你想画几条边的螺旋线？',4,3,8))
t.bgcolor('black')
color = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'orange', 'white']
t.speed(0)

for x in range(100):   #绘制大螺旋线
    t.forward(x * 4)
    position = t.position()
    heading = t.heading()
    
    for y in range(int( x / 2)): #绘制小螺旋线
        t.pencolor(color[y % sides])
        t.penup()
        t.forward(2 * y)
        t.pendown()
        for z in range(4):
            t.circle(2 * y)
        t.right(360 / sides - 2)
        t.penup()

    t.goto(position)
    t.seth(heading)
    t.left(360 // sides + 2)
t.done()

