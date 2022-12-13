import random as r
from turtle import *
from logic import five_angle_star, six_angle_star

t = Turtle()
t.shape('turtle')
t.speed(0)
t.up()

five_angle_star(t, 100)
t.goto(100, 100)
six_angle_star(t, 50)

done()