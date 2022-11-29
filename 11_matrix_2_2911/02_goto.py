import random as r
from turtle import *

t = Turtle()
t.shape('turtle')
t.speed(0)  # скорость черепашки (0 - самая большая)
colors = ['#4287f5', '#cb3deb', '#6a2f78', '#a091a3',
          '#a8256f', '#e5f78b', '#e36a19', '#e2f53d',
          '#ffb6b3', '#b3fff7', '#ffb3d4', '#f22c82',
          '#a19f38', '#ffb617', '#a19d95', '#ffffff']  # список цветов
for i in range(1000):
    t.up()  # поднять перо (перестать рисовать)
    x = r.randint(-400, 400)  # сгенерировать случайную координату x
    y = r.randint(-400, 400)  # сгенерировать случайную координату у
    t.goto(x, y)  # перейти в координаты x, y
    t.down()  # опустить перо (начать рисовать)
    t.color(r.choice(colors))  # установить цвет черепашки
    t.dot(r.randint(30, 80))

done()
