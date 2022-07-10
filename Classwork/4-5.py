# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-06 17:09:10
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:08:18
#打印乘法表
import os #防止用命令行运行窗口一闪而过
number = eval(input("你要打印几乘几的乘法表（x * x）"))
number **= 0.5
print("窗口全屏观看")
for x in range(1, int(number + 1)):
    for y in range(1, x + 1):
        print(f"%d * %d = %d" % (x , y, x *y), end = "\t")
    if x >= 10:
        for z in range(3):
            print()
    else:
        for z in range(2):
            print()

os.system("pause")
