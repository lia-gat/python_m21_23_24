m = int(input('Enter number of pages: '))
set1 = set()
set2 = set()
all_lessons = set()
n = int(input('Enter number of lines: '))

for _ in range(n):
        surname = input('Enter the surnames of the students: ')
        set1.add(surname)

for _ in range(m - 1):
    n = int(input('Enter number of lines: '))
    
    for _ in range(n):
        surname = input('Enter the surnames of the students: ')
        if surname in set1:
            set2.add(surname)
    
    set1 = set1 & set2
    set2.clear()

for i in set1:
    print(i)  
