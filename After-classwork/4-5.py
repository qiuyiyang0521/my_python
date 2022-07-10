# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-07 16:05:35
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:03:56
import os


os.system("pause")

#等差数列的问题
num = int(input("你想要计算前几项之和（输入“0”结束）"))
while num != 0:
    print(f"前%d项的和是%d"%(num, (1 + num) * num / 2))
    num = int(input("你想要计算前几项之和（输入“0”结束）"))


