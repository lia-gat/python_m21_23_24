n = int(input('Enter number: '))
num_list = []

for _ in range(n):
    num = int(input('Enter number: '))
    num_list.append(num)

for i in range(n - 1):
    print(num_list[i] + num_list[i + 1])
