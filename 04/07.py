num = int(input('Enter number: '))
a = 0

for i in range(1, num+1):
    if (num % i == 0):
        print(i, end=' ')
        a +=1

print('\n') 
if a == 2:
    print('ПРОСТОЕ')
else:
    print('НЕТ')
    