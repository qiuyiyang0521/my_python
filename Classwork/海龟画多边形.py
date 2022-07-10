# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2022-07-07 16:05:59
# @Last Modified by:   Administrator
# @Last Modified time: 2022-07-09 10:27:20
import turtle as t
a = eval(input('边数'))
t.speed(0)
if a == 3:
    for x in range(255):
        t.forward(x * 2)
        t.right(360 / a)
else:
   for x in range(500):
        t.forward(x)
        t.right(360 / a)
        
    

