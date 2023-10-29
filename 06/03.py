m = int(input('Enter number of students studying English: '))
n = int(input('Enter number of students studying German: '))
english_student, german_student = set(), set() 


for _ in range(m):
    last_name = input('Enter student\'s last name: ')
    english_student.add(last_name)
    
for _ in range(n):
    last_name = input('Enter student\'s last name: ')
    german_student.add(last_name)
        
one_lang = (english_student - german_student) | (german_student - english_student)

if len(one_lang) > 0:
    print(len(one_lang))
else:
    print('NO')