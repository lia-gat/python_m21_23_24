soup = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']

num = int(input('Enter num: '))

for i in range(num):
    print(soup[i % 5])
    
    