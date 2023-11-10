def print_document(pages):
    secret_pages = 0
    for i in pages:
        if 'Секретно' in i:
            secret_pages += 1
            print('Дальнейшие материалы засекречены')
            break
        else:
            print(i)
    if secret_pages == 0:
        print('Напечатано без купюр')
                
print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
print()
print_document(["Пустой трёп", "который", "никому не интересен"])