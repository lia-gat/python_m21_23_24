m = int(input('Enter number of students studying English: '))
n = int(input('Enter number of students studying German: '))
k = int(input('Enter number of students studying French: '))
english_student, german_student, french_student = set(), set(), set()

for _ in range(m + n + k):
    last_name = input('Enter student\'s last name: ')
    if last_name in german_student:
        french_student.add(last_name)
    elif last_name in english_student:
        german_student.add(last_name)
    else:
        english_student.add(last_name)
        
two_lang = ((english_student & german_student) - french_student) | ((german_student & french_student) - english_student) | ((french_student & english_student) - german_student)

if len(two_lang) > 0:
    print(len(two_lang))
else:
    print('NO')