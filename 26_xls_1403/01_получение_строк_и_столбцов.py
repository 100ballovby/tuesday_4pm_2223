import openpyxl as xl

wb = xl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
sheet = list(sheet)

for row in sheet:
    for cell in row:
        print(cell.coordinate, cell.value, end=' ')
    print('\n----конец строки----')

