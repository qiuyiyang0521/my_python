import time
girl_or_boy = str(input("请问你的性别是什么？"))
time.sleep(0.2)
your_age = int(input("请问你的年龄？"))
time.sleep(0.5)
if girl_or_boy == "男":
	
	if your_age >= 22:
		print("你可以结婚。")
	else:
		print("你不可以结婚。")

else:
	if your_age >= 20:
		print("你可以结婚。")
	else:
		print("你不可以结婚。")

time.sleep(0.5)
print("运行结束")	
