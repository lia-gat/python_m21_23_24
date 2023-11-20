def sorted(arr):
    a = []
    for i in range(len(arr)):
        a.append(min(arr))
        arr.remove(min(arr))
    
    print(a)
    print(id(a))
    
old_a = [1, 3, 6 , 4, 2,5]
print(id(old_a))
old_a.sort()
print(old_a)
print(id(old_a))

print('*****')

old_a = [1, 3, 6 , 4, 2, 5]
print(id(old_a))
sorted(old_a)

