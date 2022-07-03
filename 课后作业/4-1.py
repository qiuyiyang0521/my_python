import turtle as t
t.speed(0)
num = int(t.numinput("圆", "你想要画几个圆", 4, 1, 360))
t.pencolor(t.textinput("画笔颜色","你想要画出什么颜色？"))
for x in range(1, num + 1):
    t.circle(100)
    t.left(360 / num)
t.done()
print("运行结束")
