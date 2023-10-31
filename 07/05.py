first_word = list(input('Enter word: '))
second_word = list(input('Enter first word: '))

while True:
    if first_word[-1] == second_word[0]:
        first_word = second_word
        second_word = list(input('Enter first word: '))
    else:
        break
    
print(*second_word, sep='')