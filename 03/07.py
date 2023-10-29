print('Загадайте число от 1 до 1000.')
left_num = 0
right_num = 1000
current = (left_num + right_num) // 2
a = 0

while a < 10:
    print(current)
    answer = input()
        
    if answer == '>':
        left_num = current
    elif answer == '<':
        right_num = current
    elif answer == '=':
        break
    
    a += 1
    current = (left_num + right_num) // 2
