n = int(input('Enter the number of rows: '))
flag = False

for _ in range(n):
    string = input('Enter row: ')
    
    if ('кот' in string or 'Кот' in string):
        flag = True
    elif ('пёс' in string or 'Пёс' in string):
        flag = False
    
if flag is True:
    print('МЯУ')
else:
    print('НЕТ')
    

    
