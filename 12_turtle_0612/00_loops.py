import random as r
from turtle import *
from f import square, triangle, spiral, spider # импортировал функцию из файла f

t = Turtle()
t.shape('turtle')
t.speed(0)

t.up()
spiral(t, 5, 80, 200, 200, '#0e4caa')
square(t, 50, 0, 0, '#0e4caa')
triangle(t, 50, 0, 0, '#0e4caa')
square(t, 70, -100, -100, '#ff6c90')
triangle(t, 70, -100, -100, '#ff6c90')
square(t, 120, 200, 200, '#aaa33c')
triangle(t, 120, 200, 200, '#aaa33c')
spider(t, 100, 360)

done()


