import turtle
turtle.bgcolor("black")
t=turtle.Pen()
t.speed(0)
num = int(turtle.numinput("圆的个数","请输入绘制的圆的数量？",6,3,30))
for x in range(num):
    t.pencolor("red")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(50)
    t.left(360 // num)
    
print("绘制结束")
