import datetime as dt

timeNow = dt.datetime.now()  # замеряет текущие время и дату с компьютера
print(timeNow)

march8 = dt.datetime(year=2023, month=3, day=8)
print(march8.date())

jan1 = dt.datetime(year=2023, month=1, day=1)  # сохранить дату на собственных значениях
delta = march8 - jan1  # вычислить, сколько дней прошло с определенной даты
print(delta)

today = dt.date.today()  # сегодняшняя дата
before = today - dt.timedelta(days=18)  # дельта помогает считать дату
after = today + dt.timedelta(days=18)
print(f'18 дней назад было: {before}')
print(f'Через 18 дней будет: {after}')

print(f'День недели сегодня: {today.weekday()}')  # возвращает дни недели в виде числа, отсчет начинается с 0
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье',]
print(f'День недели сегодня: {days[today.weekday()]}')
