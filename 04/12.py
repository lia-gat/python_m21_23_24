n = int(input('Enter numbers: '))
summ = 0
c = 0

for _ in range(n):
    num = int(input('Enter number: '))
    c += 1
    
    if c % 2 == 0:
        summ -= num
    else:
        summ += num

print(summ)    