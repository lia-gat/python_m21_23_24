num = int(input('Enter num: '))
c = 0
summ = 0
num_str = -1

while num != 0:
    c += 1
    summ += num
    
    if summ == 10:
        num_str = c
    
    num = int(input('Enter num: '))    

print(num_str)