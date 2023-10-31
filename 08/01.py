word = input('Enter word:')
max_word = word
min_word = word

while word != 'стоп':
    if len(word) > len(max_word):
        max_word = word
    if len(word) < len(min_word):
        min_word = word
    word = input('Emter word:')

max_word , min_word  = set(max_word), set(min_word)

for i in min_word:
    if i not in max_word:
        print('НЕТ')
        break
else:
    print('ДА')
    