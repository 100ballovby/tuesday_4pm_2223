def square(obj, length, x, y):
    obj.goto(x, y)
    obj.down()
    for i in range(4):
        obj.fd(length)
        obj.lt(90)
    obj.up()


def five_angle_star(obj, length):
    obj.down()
    for i in range(5):
        obj.fd(length)
        obj.rt(144)
    obj.up()


def six_angle_star(obj, length):
    obj.down()
    for i in range(6):
        obj.fd(length)
        obj.lt(45)
        obj.fd(length)
        obj.rt(105)
    obj.up()