import turtle as t
t.bgcolor("black")
t.speed(0)
t.ht()
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "pink"]
family = []
name = t.textinput("我的家庭", "输入家庭成员的名字（直接按回车结束）")

while name != "":
    family.append(name)
    name = t.textinput("我的家庭", "输入家庭成员的名字（直接按回车结束）")

for x in range(1, 101):
    t.pencolor(colors[x % len(family)])
    t.up()
    t.forward(x * 4)
    t.down()
    t.write(family[x % len(family)], font = ("黑体", int((x + 4) // 4), "bold"))
    t.left(360 / len(family) + 2)
t.done()

print("绘制结束")
