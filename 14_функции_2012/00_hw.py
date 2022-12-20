from turtle import *


def square(obj, length):
    obj.down()
    for i in range(4):
        obj.fd(length)
        obj.rt(90)
    obj.up()


t = Turtle()
t.speed(0)

n = int(input('Введите количество квадратов: '))

for i in range(n):
    square(t, 100)
    t.fd(100)

done()
