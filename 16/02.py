def larger_root(p,q):
    d = discriminant(1, p,q)
    return (-p + d ** 0.5) / 2

def smaller_root(p,q):
    d = discriminant(1, p,q)
    return (-p - d ** 0.5) / 2

def discriminant(a, b, c):
    return b **2 - 4 * a * c
    
def main():
    p = float(input('Enter number: '))
    q = float(input('Enter number: '))
    
    print(discriminant(1, p, q))
    print(larger_root(p, q), smaller_root(p, q))
    
    print(smaller_root(2, 1))
    print(larger_root(2, 1))

main()
