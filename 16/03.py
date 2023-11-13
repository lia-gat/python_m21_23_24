old_message = ''

def print_without_duplicates(message):
    global old_message
    if message != old_message:
        old_message = message
        print(message)
    else:
        pass
    
print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Когда доедешь до дома")
print_without_duplicates("Ага, жду")
print_without_duplicates("Ага, жду")