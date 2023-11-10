def num_digits(number):
    c = 0
    for _ in range(len(str(number))):
        c +=1
    return c
    
print(num_digits(1))

print(num_digits(157))