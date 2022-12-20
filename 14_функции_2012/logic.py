def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    try:  # попробовать
        return a / b  # вернуть результат деления a на b
    except ZeroDivisionError:  # при возникновении исключения "деление на 0"
        return 0  # вернуть 0


