def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')

def search_card(name):
    for i in range(len(base)):
        if base[i] == name:
            print(f'Ваша карта с номером {i + 1} найдена')
            break
        else:
            print('Ваша карта не найдена')
            break

base = ["Иван", "Юлия Иванкова"]

hello("Иван")
search_card("Иван")
hello("Юлия Иванова")
search_card("Юлия Иванова")
