import turtle as t
sides = int(t.numinput('边数','你想画几条边的螺旋线？',4,3,8))
t.bgcolor('black')
color = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'orange', 'white']
t.speed(0)
for x in range(250):
    t.pencolor(color[x % sides])
    t.forward(x / 2)
    t.right(360 // sides + 1)
