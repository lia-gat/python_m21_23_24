calendar = dict()

num = int(input('Enter number: '))

for _ in range(num):
    name, number, month = input('Enter information about birthdays: ').split()
    if month not in calendar:
            calendar[month] = [name]
    else:
       calendar[month].append(name)
    
num = int(input('Enter number: '))

for _ in range(num):
    month = input('Enter month: ')
    if month in calendar:
        print(*calendar[month])
    else:
        print()