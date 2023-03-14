import openpyxl as xl

wb = xl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

us_pop = 0

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    popul = sheet['D' + str(row)].value

    us_pop += popul

    # агрантия существования ключа для штата. У каждого штата будет свой словарь, в котором будут храниться значения округов и популяции
    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'pop': 0, 'tracts': 0})

    # каждая строка - один переписной район, поэтому увеличиваем счетчик районов на 1
    county_data[state][county]['tracts'] += 1
    # увеличим численность населения округа на численность населения района
    county_data[state][county]['pop'] += popul

print(county_data)
print(f'The population of the USA: {us_pop}')
