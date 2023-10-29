days = int(input('Enter number days: '))
t = []
a = 0

for i in range(days):
    day = float(input('Enter t: '))
    if day > 22.0:
        a += 1

print(f'Days: {a // 7}')







