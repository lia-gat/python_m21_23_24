num = int(input('Enter number: '))
lines_list = []

for _ in range(num):
    line = input('Enter shopping: ')
    lines_list.append(line)

search_n = int(input('Enter n: '))
search_list = []

for _ in range(search_n):
    search = input('Enter: ')
    search_list.append(search) 

for i in lines_list:
    flag = True
    for j in search_list:
        if j not in i:
            flag = False
    if flag:
        print(i)
   