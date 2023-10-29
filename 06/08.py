n = int(input('Enter the number of men: '))
men = set()
namesake = set()
c = 0

for _ in range(n):
    surname = input('Enter the man\'s surname: ')
    if surname in men and surname not in namesake:
        c += 2
        namesake.add(surname)
    elif surname in men:
        if surname in namesake:
            c += 1
        namesake.add(surname)        
    men.add(surname)   
    
print(c)

