def spawnNumber():
    numb = []
    temp = []
    mostTemp = []
    most = 0

    addNumb = 'Y'

    while addNumb != 'X':
        addNumb = input("Input your number (klik 'X' or fill blank to print): ")
        if addNumb and addNumb != 'x' and addNumb != 'X' and addNumb != '':
            numb.append(addNumb)
        
        if addNumb == 'X' or addNumb == '' or addNumb == 'x':
            break
        
    print('\nYour input number is: ', end='')
    for i in range(0, len(numb)):
        temp.clear()
        print(numb[i], end=" ")
        for j in range(0, len(numb)):
            if numb[i] == numb[j]:
                temp.append(numb[j])
        
        mostTemp = len(temp)
        if most < mostTemp:
            most = mostTemp
            theNumber = temp[0]

    print(f'\nMost spawn number is {theNumber}, appears as {most} times')

spawnNumber()