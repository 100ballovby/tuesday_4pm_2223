import time
print("Чтобы начать отсчет времени, нажмите ENTER. Чтобы остановить, нажмите Ctrl+C")

input()  # блокировать исполнение кода, пока что-то не введут

print('Отсчет начат!')
start = time.time()
lastTime = start
lapNum = 1

# начало отслеживания замеров секундомером
try:
    while True:
        input()  # новый отсчет времени
        lapTime = round(time.time() - lastTime, 2)
        totaltime = round(time.time() - start, 2)
        print(f'Замер {lapNum}: {totaltime} {lapTime}')
        lapNum += 1
        lastTime = time.time()  # переустановить время последнего замера
except KeyboardInterrupt:
    print('Готово!')

