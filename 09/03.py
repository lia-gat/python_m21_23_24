num = int(input('Enter number: '))
lines_list = []
word_list = []

for _ in range(num):
    line = input('Enter shopping: ')
    lines_list.extend(line)
    word_list.append(lines_list)
    lines_list = []


search = int(input('Enter: '))-1

for i in range(num):
    print(word_list[i][search], end='') 

