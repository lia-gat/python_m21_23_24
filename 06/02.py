num = int(input('Enter number: '))
c = 0
cities = set()
flag = True

for _ in range(num + 1):
    city = input('Enter city: ')
    c += 1
    if city not in cities:
        cities.add(city)
    else:
        flag = False   
    
if flag:
    print('OK')
else:
    print('TRY ANOTHER')