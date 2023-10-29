first_str = float(input('Enter first string: '))
second_str = float(input('Enter second string: '))
third_str = input('Enter third string: ')

if third_str == '+':
    print(first_str + second_str)
elif third_str == '-':
    print(first_str - second_str)
elif third_str == '*':
    print(first_str * second_str)
elif third_str == '/':
    if second_str == 0:
        print(88888)
    else:
        print(first_str / second_str)
else:
    print(888888)