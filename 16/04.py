count = 0
count_items = 0
items = []
cost = 0

def add_item(item_name, item_cost):
    global items, count_items, cost
    item_and_cost = item_name + ' - ' + str(item_cost)
    items.append(item_and_cost)
    count_items += 1
    cost += item_cost

def print_receipt():
    global count, items, count_items, cost
    if count_items != 0:
        count += 1
        print(f'Чек {count} Всего предметов: {count_items}')
        print(*items, sep='\n')
        print(f'Итого: {cost}')
        print('-----')
        count_items = 0
        items = []
        cost = 0

add_item('Блокнот', 100)
print_receipt()
add_item('Ручка', 70)
print_receipt()
print_receipt()
add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()
add_item('Булочка', 15)
add_item('Булочка', 15)
# (Отменить чек) - этот чек не печатаем