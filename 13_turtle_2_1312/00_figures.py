import random as r
from turtle import *
from logic import square

t = Turtle()
t.shape('turtle')
t.speed(0)

l = 10
x = 0
y = 0

for i in range(10):
    l += 10
    x -= 5
    y -= 5
    square(t, l, x, y)


done()


