c = 0
num_str = -1
summ = 0

while True:
    string = input('Enter row: ')
    c += 1
    if 'кот' in string:
        num_str = c
        summ += 1
        
    elif 'СТОП' in string:
        break
            
print(summ, '\t',  num_str)