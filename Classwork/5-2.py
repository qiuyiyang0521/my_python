import os

driving_age = int(input("法定的驾车年龄是多少岁？"))
your_age = int(input("你几岁了？"))
if your_age >= driving_age:
	print("你已经达到了驾车年龄，如果你有驾照，就可以开车上路了。")

else:
	print("你没有达到驾车年龄，你至少要等{d}年才能开车上路呦。".format(driving_age - your_age))

	os.system("pause")
