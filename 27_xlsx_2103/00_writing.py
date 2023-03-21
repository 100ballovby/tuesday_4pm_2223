from openpyxl import Workbook


def print_rows():
    for row in sheet.iter_rows(values_only=True):  # выводить только ячейки со значениями
        print(row)


filename = 'hello.xlsx'

wb = Workbook()
sheet = wb.active  # создали лист в таблице

sheet['A1'] = 'hello'
sheet['B1'] = 'world!'

print_rows()

sheet['A1'] = 'Good bye'
sheet['B10'] = 'test'

print_rows()

sheet.insert_cols(idx=1)  # вставить колонку перед первой колонкой
print_rows()

sheet.insert_cols(idx=3, amount=5)  # вставить 5 колонок перед третьей
print_rows()

sheet.delete_cols(idx=1) # удалить первую колонку
print_rows()

sheet.delete_cols(idx=2, amount=5)  # удалить 5 колонок
print_rows()

wb.save(filename)
