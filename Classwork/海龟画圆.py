import turtle as t
a = eval(input('圆的个数'))
t.speed(0)
t.bgcolor('black')
for x in range(a):
    t.pencolor('yellow')
    t.circle(200)
    t.right(360 / a)
    t.pencolor('red')
    t.circle(100)
    t.right(360 / a)

