num = int(input('Enter number: '))
lines_list = []

for _ in range(num):
    line = input('Enter shopping: ')
    lines_list.append(line)

search = input('Enter: ')

for i in lines_list:
    if search in i:
        print(i)