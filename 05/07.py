war = 'Евразия'
peace = 'Остазия'
num = int(input('Enter number of commands: '))

for _ in range(num):
    command = input('Enter the command: ')
    if command == 'С кем война?':
        print(war)
    elif command == 'С кем мир?':
        print(peace)
    elif command == 'Меняем':
        war, peace = peace, war
        
        