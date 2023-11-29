def summ_sqrt(array):
    return (sum(map(lambda x: x**2, filter(lambda x: not x%9, array))))


def main():
    print(summ_sqrt(range(10,100)))
    
    
main()