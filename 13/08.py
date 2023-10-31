num = int(input('Enter num: '))
dictionary = dict()

for _ in range(num):
    text = input('Enter the word and its meaning: ').split()
    word = text[0]
    text.remove(word)
    dictionary[word] = ' '.join(text)

num = int(input('Enter num: '))

for _ in range(num):
    word = input('Enter word: ')
    if word in dictionary:
        print(dictionary[word])
    else:
        print('Нет в словаре') 
