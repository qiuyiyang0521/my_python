
# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-07 09:09:37
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 16:39:03
import turtle as t
t.hideturtle()
t.speed(10)
t.up()
t.goto(0, -200)
t.down()
t.circle(200)
t.up()
t.goto(-100,50)
t.down()
t.fillcolor("blue")
t.begin_fill()
t.circle(20)
t.end_fill()
t.up()
t.seth(0)
t.forward(200)
t.down()
t.begin_fill()
t.circle(20)
t.end_fill()
t.up()
t.goto(0, 50)
t.down()
t.circle(-50, steps = 3)
t.up()
t.goto(-150, -70)
t.down()
t.goto(0, -170)
t.goto(-150 + 300, -70)
t.penup()
t.done()
