borya = int(input('Введите рост Бори: '))
vova = int(input('Введите рост Вовы: '))
dima = int(input('Введите рост Димы: '))

height = [borya, vova, dima]

height.sort(reverse=True)
for h in height:
    print(h)