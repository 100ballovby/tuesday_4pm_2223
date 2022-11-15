guests = ['Alex', 'Julia', 'Peter']

for name in guests:
    print(name, 'you have invited to my lunch.')

name = input('Input name: ')
print(name, 'left.')
guests.remove(name)
name = input('New guest: ')
guests.append(name)

for name in guests:
    print(name, 'you have invited to my lunch.')

print('There are 3 new guests!')
guests.insert(0, 'John')
guests.insert(2, 'Molly')
guests.append('Will')

print('Sorry. I can invite only 2 guests.')
i = 0
while len(guests) > 2:
    print(guests[i], 'sorry.')
    guests.pop(i)

print(guests)
