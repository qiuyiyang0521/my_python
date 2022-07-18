import turtle as t
answer = str(input("你想要画一个圆吗"))
if answer == "y" or answer == "yes" or answer == "YES" or answer == "Yes":
	print("开始绘制...")
	t.width(3)
	t.circle(200)
	print("绘制结束...")
print("运行结束")