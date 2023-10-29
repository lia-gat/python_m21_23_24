m = int(input('Enter the number of books in your home library: '))
n = int(input('Enter the number of books in the list for the summer: '))
books = set()

for _ in range(m):
    book = input('Enter the name of the book in your home library: ')
    books.add(book)
    
for _ in range(n):
    book = input('Enter the name of the book in the list for the summer: ')
    if book in books:
        print('Yes')
    else:
        print('No')
    
