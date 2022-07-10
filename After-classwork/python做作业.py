# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-03 09:20:38
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:04:55

a = input('输入题目，或按’Q’退出')
while a != 'q':
	print(a, '=', eval(a))
	a = input('输入题目，或按’Q’退出')

print('再见！')
