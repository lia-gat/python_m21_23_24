password1 = input('Enter your password: ')
password2 = input('Repeat your password: ')
a = 0    

while a < 1:
    if len(password1) < 8:
        print('Короткий')
        break
    
    if '123' in password1:
        print('Простой')
        break
    
    if password1 != password2:
        print('Различаются')
        break
    
    a +=1
    print('OK')  