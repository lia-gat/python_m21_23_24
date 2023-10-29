n = int(input('Enter the number of people being tested: '))
average_iq = 0

for i in range(1, n+1):
    human_iq = int(input('Enter human IQ: '))
    average_iq += human_iq
    average = average_iq / i
    
    if average == human_iq:
        print('0')
    elif human_iq > average:
        print('average: >')
    elif human_iq < average:
        print('average: <')
  
    
    
        



    