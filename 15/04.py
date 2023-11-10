def average(values):
    if len(values) == 0:
        print(0)
    else:
        summ = 0
        for i in range(len(values)):
            summ+=values[i]
        average_value=summ/len(values)
        return average_value

print(average([1, 5, 500, 10]))

print(average([1, 2, 3, 4, 5]))

print(average([-5, 2]))



