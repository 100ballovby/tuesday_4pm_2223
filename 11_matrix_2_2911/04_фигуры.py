import random as r
from turtle import *

t = Turtle()
t.shape('turtle')

# нарисовать квадрат
for i in range(4):
    t.fd(100)
    t.rt(90)

# нарисовать треугольник
for i in range(3):
    t.fd(100)
    t.lt(120)

done()
