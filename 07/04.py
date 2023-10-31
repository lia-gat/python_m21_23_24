first_word = list(input('Enter first word: '))
second_word = list(input('Enter second word: '))

if first_word[-1] == second_word[0]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')