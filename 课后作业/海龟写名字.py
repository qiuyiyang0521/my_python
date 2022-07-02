import turtle as t

t.bgcolor('black')
t.speed(0)
your_name = t.textinput("名字","请输入你的名字")
sides = int(t.numinput("边数","你想要几条边的螺旋线？",4,3,8))
colors = ["red","yellow","green","blue","purple","pink","orange","white"]
for x in range(100):
    t.pencolor(colors[x % sides])
    t.up()
    t.forward(x * 4)
    t.down()
    t.write(your_name, font =("宋体", 12, "bold"))
    t.left(360 / sides + 1)


print("绘制结束")

