,import turtle as t


t.penup()
sides = int(t.numinput('边数','你想画几条边的螺旋线？',4,3,8))
t.bgcolor('black')
color = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'orange', 'white']
t.speed(0)

for x in range(100):   #绘制大螺旋线
    t.forward(x * 4)
    position = t.position()
    heading = t.heading()
    
    for y in range(int( x / 2)): #绘制小螺旋线
        t.pendown()
        t.pencolor(color[y % sides])
        t.forward(2 * y)
        t.right(360 / sides - 2)
        t.penup()

    t.goto(position)
    t.seth(heading)
    t.left(360 // sides + 2)
t.done()
