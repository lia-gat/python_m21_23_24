product = 1

for _ in range(6):
    num = int(input('Enter number:'))
    if num != 0:
        product *= num
        
print(product)