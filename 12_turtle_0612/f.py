def square(obj, side, x, y, col):
    """
    Функция рисует квадрат
    :param obj: тот, ктоо будет рисовать (черепашка)
    :param side: длина стороны квадрата
    :param x: координата х
    :param y: координата y
    :param col: цвет
    :return: None
    """
    obj.goto(x, y)  # переходим в координаты
    obj.color(col)  # устанавливаем цвет рисования
    obj.down()  # опустим перо (начать рисовать)
    for i in range(4):  # рисуем квадрат
        obj.fd(side)
        obj.rt(90)
    obj.up()  # поднять перо (перестать рисовать)


def triangle(obj, side, x, y, col):
    """
    Функция рисует треугольник
    :param obj: тот, ктоо будет рисовать (черепашка)
    :param side: длина стороны квадрата
    :param x: координата х
    :param y: координата y
    :param col: цвет
    :return: None
    """
    obj.goto(x, y)  # переходим в координаты
    obj.color(col)  # устанавливаем цвет рисования
    obj.down()  # опустим перо (начать рисовать)
    for i in range(3):  # рисуем квадрат
        obj.fd(side)
        obj.lt(120)
    obj.up()  # поднять перо (перестать рисовать)


def spiral(obj, side, deg, x, y, col):
    """
    Функция рисует квадрат
    :param obj: тот, ктоо будет рисовать (черепашка)
    :param side: длина стороны квадрата
    :param deg: количество градусов поворота
    :param x: координата х
    :param y: координата y
    :param col: цвет
    :return: None
    """
    obj.goto(x, y)  # переходим в координаты
    obj.color(col)  # устанавливаем цвет рисования
    obj.down()  # опустим перо (начать рисовать)
    for i in range(100):  # рисуем квадрат
        obj.fd(side + i * 2)
        obj.rt(deg)
    obj.up()  # поднять перо (перестать рисовать)


def spider(obj, length, n):
    obj.down()

    for i in range(n):
        obj.fd(length)
        obj.stamp()  # оставить след черепашкой
        obj.bk(length)
        obj.lt(360 / n)
    obj.up()
