import csv
import json


def read_csv(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as table:
        reader = csv.reader(table)
        for line in reader:
            lines.append(line)
    return lines[1:]  # убираем первый элемент списка, оставляем все со второго до конца


def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8') as table:
        writer = csv.writer(table)
        writer.writerows(data)


def get_headers(filename):
    with open(filename, 'r', encoding='utf-8') as table:
        lines = table.readlines()
        reader = csv.DictReader(lines)
        return reader.fieldnames

def csv_to_json(data, json_file, keys):
    """
    Функция преобразовывает данные из CSV таблицы в формат файла JSON
    :param data: данные CSV-файла,
    :param json_file: имя файла для записи
    :param keys: хедеры таблицы
    """
    res = []  # список, в котором будут храниться все элементы JSON
    for i in range(len(data)):  # циклом просматриваю данные CSV-файла
        dct = {}  # словарь, который буду добавлять в список
        for j in range(len(data[i])):  # просматриваю каждый элемент списка из CSV
            try:
                info = eval(data[i][j])  # пытаюсь преобразовать данные
            except:
                info = data[i][j]  # если не получилось, закидываю как есть
            dct[keys[j]] = info  # ключ - из хедеров, данные из CSV
        res.append(dct)
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(res, indent=4))
    return res



headers = get_headers('bestsellers_with_categories_2022_03_27.csv')
print(headers)
data = read_csv('bestsellers_with_categories_2022_03_27.csv')
print(data)

books = csv_to_json(data, 'books.json', headers)
for book in books:
    if 10000 <= book['Reviews'] <= 30000:
        print(book['Name'], book['Author'], book['User Rating'])

