import turtle as t
t.speed(0)
t.bgcolor("black")
num = int(t.numinput("圆", "你想要画几个圆", 4, 1, 360))
for x in range(1, num + 1):
    t.pencolor("red")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(50)
    t.left(360 / num)
t.done()

print("运行结束")
