import os

# создание папки
dir = 'my_directory'  # Название папки
os.mkdir(dir)  # создать папку
for i in range(10):  # в цикле на 10 повторений
    filename = f'file_{i}.txt'
    path = os.path.join(dir, filename)  # Объединяю путь к папке с именем файла
    file = open(path, 'w')  # сохраняю файл по пути path
    file.write(f'Содержимое файла №{i}.')  # Записать текст
    file.close()



