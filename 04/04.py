numbers = int(input("Enter number:"))
product = 1

for num in range(2, numbers+1):
    product *= num
    
print(product)
