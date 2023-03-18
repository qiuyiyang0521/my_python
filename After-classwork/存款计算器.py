money = eval(input('金额：'))
li_lv = eval(input('利率：'))
years = eval(input('年数：'))
print(f'%d年后的金额是%d' % (years, money * ((1 + li_lv) ** years)))
