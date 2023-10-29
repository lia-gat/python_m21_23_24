n = int(input('Enter the number of rows: '))
string = ''

for _ in range(n):
    string += input()
    
if 'кот' in string:
    print('МЯУ')
else:
    print('НЕТ')