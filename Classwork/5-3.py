import time

num = int(input("请输入一个整数"))
time.sleep(0.5)
if num % 2 == 0:
	print("它是一个偶数")
else:
	print("它是一个奇数")

time.sleep(0.5)
print("运行结束")
