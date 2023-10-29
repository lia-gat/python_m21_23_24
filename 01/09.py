login = input('Enter login: ')
email = input('Enter email: ')

if ('@' not in email or '@' in login):
    print('Ошибка')
else:
    print('OK')
    
