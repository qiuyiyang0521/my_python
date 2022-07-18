import turtle
answer = str(input("你想要绘制一个螺旋线吗？(y/n)"))
if answer == "y":
	for x in range(100):
		t.forward(x * 2)
		t.right(360 / 4 + 1)
	t.done()
else:
	print("感谢你使用这个程序！")

os.system("pause")
