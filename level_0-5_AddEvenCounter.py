namba = []

def Counter():

    while True:
        numbs = input('Input Your Number (fill blank or type "x" to close): ')
        if numbs != 'x' and numbs != '':
            namba.append(numbs)
        if numbs == 'x' or numbs == '':
            break
        
    print("All your number is: ", end="")
    for i in range(0, len(namba)):
        print(namba[i], end=" ")

Counter()
