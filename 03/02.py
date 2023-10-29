password1 = input('Enter your password: ')
password2 = input('Repeat your password: ')
a = 0    

while a < 1:
       
    if len(password1) < 8:
        print('Короткий')
        break
    else:
        a += 1

    if password1 != password2:
        print('Различаются')
        break
    else:
        a += 1
    
    print('OK')    
        
      


    




