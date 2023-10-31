text = list(input('Enter text: '))
answer = []

for i in text:
    code = ord(i)
    answer.append(code)
    
print(*answer, sep=', ')