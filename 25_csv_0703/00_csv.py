import csv


def read_csv(filename):
    lines = []
    with open(filename, 'r') as table:
        reader = csv.reader(table)
        for line in reader:
            lines.append(line)
    return lines[1:]  # убираем первый элемент списка, оставляем все со второго до конца


def write_csv(filename, data):
    with open(filename, 'w') as table:
        writer = csv.writer(table)
        writer.writerows(data)


def get_headers(filename):
    with open(filename, 'r') as table:
        lines = table.readlines()
        reader = csv.DictReader(lines)
        return reader.fieldnames


headers = get_headers('bestsellers_with_categories_2022_03_27.csv')
print(headers)
data = read_csv('bestsellers_with_categories_2022_03_27.csv')
print(data)
