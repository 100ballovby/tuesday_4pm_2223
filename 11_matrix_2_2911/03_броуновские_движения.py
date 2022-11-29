import random as r
from turtle import *

t = Turtle()
t.shape('turtle')
t.speed(-1000)
t.pensize(3)

colors = ['#4287f5', '#cb3deb', '#6a2f78', '#a091a3',
          '#a8256f', '#e5f78b', '#e36a19', '#e2f53d',
          '#ffb6b3', '#b3fff7', '#ffb3d4', '#f22c82',
          '#a19f38', '#ffb617', '#a19d95', '#ffffff']

for i in range(1000):
    step = r.randint(-20, 20)
    turn = r.randint(-180, 180)
    t.color(r.choice(colors))
    t.fd(step)
    t.rt(turn)

done()
