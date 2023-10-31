num = int(input('Enter number: '))
lines_list = []
num_list = []

for _ in range(num):
    line = input('Enter shopping: ')
    lines_list.append(line)

num_lines = int(input('Enter num lines: ')) 

for _ in range(num_lines):
    num_line = int(input("Enter num line: ")) -1
    num_list.append(num_line)

for i in num_list:
    print(lines_list[i])