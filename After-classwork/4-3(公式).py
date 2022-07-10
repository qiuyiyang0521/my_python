# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-06 11:40:37
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:03:55
import os


os.system("pause")

num = int(input("你想要计算前几项的和"))
print(f"前%d项的和是：%d" %(num, (1 + num) * num / 2))
