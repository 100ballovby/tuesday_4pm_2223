from turtle import *


def x_angle(obj, length, x, y, n):
    obj.goto(x, y)
    obj.down()
    for i in range(n):
        obj.fd(length)
        obj.lt(360 / n)
    obj.up()

t = Turtle()
t.speed(0)

t.up()

x_angle(t, 50, -100, 100, 4)
x_angle(t, 50, -100, 200, 3)
x_angle(t, 50, 200, 200, 5)
x_angle(t, 50, 320, -320, 8)
x_angle(t, 50, -400, 250, 12)

done()
