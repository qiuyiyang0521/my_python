#画num个圆
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
num = int(turtle.numinput("圆的个数","请输入你要绘制的圆的个数",6,3,30))
for x in range(num):
    t.pencolor("red")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(50)
    
    t.left(360//num)

print("运行结束") #这句话不再循环的控制范围内
