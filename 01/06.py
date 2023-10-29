firstq = input('Любите ли вы котиков?\n')
secondq = input('Умеете ли вы программировать?\n')

if firstq == 'да':
    if secondq == 'да':
        print('Вы обладаете незаурядным умом.')
    elif secondq == 'нет':
        print('Вы обладаете заурядным умом.')
    else:
        print('Ошибка')
elif firstq == 'нет':
    if secondq == 'да':
        print('Вы не обладаете незаурядным умом.')
    elif secondq == 'нет':
        print('Вы не обладаете  умом.')
    else:
        print('Ошибка')
else:
    print('Ошибка')