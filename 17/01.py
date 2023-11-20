def parrot(phrase):
    if phrase in  words_parrot:
        print(phrase)
    else:
        words_parrot.append(phrase)

words_parrot = []
parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")

print('*****')

words_parrot = []
parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")
