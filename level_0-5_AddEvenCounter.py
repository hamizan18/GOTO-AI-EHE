def Counter():
    namba = []
    odd = 0
    even = 0

    while True:
        numbs = input('Input Your Number (fill blank to close): ')
        if numbs != '':
            numbs = int(numbs)
            if numbs % 2 == 0:
                even += 1
            else:
                odd += 1
            namba.append(numbs)
        if numbs == '':
            break
        
        
    print("All your number is: ", end="")
    for i in range(0, len(namba)):
        print(namba[i], end=" ")

    print(f"\nTotal count of Odd number is: {odd}")
    print(f"Total count of Even number is: {even} ")

Counter()