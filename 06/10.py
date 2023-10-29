m = int(input('Enter number of dishes: '))
all_dishes = set()
answer = []

for _ in range(m):
    dish = input('Enter the dish: ')
    all_dishes.add(dish)
    
n = int(input('Enter the number of days: '))
uncooked_dishes = all_dishes

for _ in range(n):
    num = int(input('Enter number of dishes: '))
    dishes = set()
    for _ in range(num):
        dish = input('Enter the dish: ')
        dishes.add(dish)
    
    uncooked_dishes -= dishes

print(*uncooked_dishes, sep='\n')