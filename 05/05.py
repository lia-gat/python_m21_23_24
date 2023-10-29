c = 0
num_str = -1

while True:
    string = input('Enter row: ')
    c += 1
    if 'кот' in string:
        num_str = c
        break
    elif 'СТОП' in string:
        break
            
print(num_str)