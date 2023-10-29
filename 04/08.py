num = int(input('Enter number: '))

for i in range(num, -1, -1):
    print(f'Осталось секунд: {i}')
else:
    print('Пуск')