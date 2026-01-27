def Counter():
    namba = []
    odd = 0
    even = 0

    while True:
        numbs = int(input('Input Your Number (fill blank to close): '))
        if numbs != '':
            if numbs % 2 == 0:
                odd += 1
            else:
                even += 1
            namba.append(numbs)
        if numbs == '':
            break
        
        
    print("All your number is: ", end="")
    for i in range(0, len(namba)):
        print(namba[i], end=" ")

    print("Total count of Odd number is: " + odd)
    print("Total count of Even number is: " + even)

Counter()
# AA PLISSS LIAT NI PENGEN LANJUUTS