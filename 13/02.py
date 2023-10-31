num = int(input('Enter num: '))
phone_book = dict()

for _ in range(num):
    phone_num, name = input('Enter phone number and name: ').split()
    if name in phone_book:
        phone_book[name].append(phone_num)
    else:
        phone_book[name] = [phone_num]

num = int(input('Enter num: '))    
for _ in range(num):
    name = input('Enter name: ') 
    if name in phone_book:
        phone_nums = ' '.join(phone_book[name])
        print(phone_nums)
    else:
        print('Нет в телефонной книге')