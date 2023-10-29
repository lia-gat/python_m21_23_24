m = int(input('Enter the number of products in the refrigerator: '))
products_in_refrigerator = set()
answer = []

for _ in range(m):
    product = input('Enter the product name: ')
    products_in_refrigerator.add(product)

n = int(input('Enter the number of recipes: '))

for _ in range(n):
    recipe = input('Enter name of the recipe: ')
    recipes = set()
    num = int(input('Enter number of ingredients: '))
    for _ in range(num):
        ingredient = input('Enter ingredient: ')
        recipes.add(ingredient)
    if recipes.issubset(products_in_refrigerator): # .issubset() - является ли набор подмножеством другого набора или нет
        answer.append(recipe)

print(*answer, sep='\n')
