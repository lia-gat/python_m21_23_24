num = int(input('Enter number: '))
shopping_list = []

for _ in range(num):
    shopping = input('Enter shopping: ')
    shopping_list.append(shopping)

for i in shopping_list:
    print(i)
