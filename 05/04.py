n = int(input('Enter the number of rows: '))
       
while n > 0:
    string = input()
    if 'кот' in string:
        print('МЯУ')
        break
    else:
        n -= 1
else:
    print('НЕТ')
    
    