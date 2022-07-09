# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-03 09:20:38
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:04:59

import turtle as t
a = eval(input('圆的个数'))
t.speed(0)
t.bgcolor('black')
for x in range(a):
    t.pencolor('yellow')
    t.circle(200)
    t.right(360 / a)
    t.pencolor('red')
    t.circle(100)
    t.right(360 / a)

