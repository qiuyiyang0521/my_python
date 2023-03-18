import turtle as t  #导入模块
t.bgcolor("black")
t.speed(0)
your_name = t.textinput("输入你的名字", "你叫什么名字？")
sides = int(t.numinput("边数", "你想要绘制几条边的螺旋线？", 4, 3, 8))
colors = ["red", "yellow", "blue", "green", "purple", "pink", "orange", "white"]
for x in range(100):
    t.pencolor(colors[x % sides])
    t.up()
    t.forward(x * 4)
    t.down()
    t.write(your_name, font = ("宋体", int(x + 4) // 4, "bold"))
    t.left(360 / sides + 1)
    t.width(x * sides / 200)

print("绘制结束")

