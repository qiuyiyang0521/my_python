# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-03 09:20:38
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 12:04:56

money = eval(input('金额：'))
li_lv = eval(input('利率：'))
years = eval(input('年数：'))
print(f'%d年后的金额是%d' % (years, money * ((1 + li_lv) ** years)))
