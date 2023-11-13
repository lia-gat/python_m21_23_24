old_message = []

def print_only_new(message):
    global old_message
    message = message.split()
    if message[-1] not in old_message:
        print(*message)
        old_message.append(message[-1])

print_only_new('Шутка номер 15')
print_only_new('Шутка номер 23')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 100')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 99')
print_only_new('Шутка номер 15')
print_only_new('Шутка номер 100')
