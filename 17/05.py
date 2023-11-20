def mirror(arr):
    mirrored_part =  arr.copy()
    mirrored_part.reverse()
    arr += mirrored_part
    return arr
    
arr = [1, 2]
mirror(arr)
print(*arr)

print('*****')

arr = [1]
mirror(arr)
print(*arr)