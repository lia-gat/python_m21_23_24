words = dict()
answer = []

text = input('Enter text: ').split()

for i in text:
    if i not in words:
        words[i] = 1
    else:
        words[i] += 1
    answer.append(words[i])
    
print(*answer)