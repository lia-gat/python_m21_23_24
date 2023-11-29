def arithmetic_operation(operation):
    if operation == '+':
        return lambda x,y: x+y
    elif operation == '-':
        return lambda x,y: x-y   
    elif operation == '*':
        return lambda x,y: x*y
    elif operation == '/':
        return lambda x,y: x/y
    


def main():
    operation = arithmetic_operation('+')
    print(operation(1, 4))


main()