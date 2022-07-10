# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-03 09:20:38
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:04:59

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
        
    

