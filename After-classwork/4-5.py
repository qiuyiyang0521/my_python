#等差数列的问题
num = int(input("你想要计算前几项之和（输入“0”结束）"))
while num != 0:
    print(f"前%d项的和是%d"%(num, (1 + num) * num / 2))
    num = int(input("你想要计算前几项之和（输入“0”结束）"))


