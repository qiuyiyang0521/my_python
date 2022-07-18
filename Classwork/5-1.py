import turtle as t
import os
answer = str(input("你想要绘制一个圆吗？(y/n)"))
if answer == "y":
	t.circle(100)
	t.done()
else:
	print("感谢你使用这个程序！")

os.system("pause")
