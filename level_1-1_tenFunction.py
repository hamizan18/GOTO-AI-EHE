# FUNCTION
def summation():
    res = 0
    maximum = int(input('Input max input number: '))
    
    for i in range(0, maximum):
        total = int(input(f'Number-{i+1}: '))
        res = int(res + total)
    
    print(f'The summation from your input is: {res}')
    
def minMax():
    allNumber = []
    button = False
    
    while True:
        try:
            firstNum = input('Input Your number (fill blank to close): ')
            if firstNum == '':
                print('Program closed.')
                break
            else:
                firstNum = int(firstNum)
                allNumber.append(firstNum)
                minNum = firstNum
                maxNum = firstNum
                button = True
            break
        except ValueError:
            print('Error, You can just input number!')
            
    if button == True:
        while True:
            try:
                n = input('Input Your number (fill blank to close): ')
                if n == '':
                    break
                else:
                    n = int(n)
                    allNumber.append(n)
            except ValueError:
                print('Error, You can just input number!')

            if n > maxNum:
                maxNum = n
            if n < minNum:
                minNum = n
        
        print('\nAll Your inputted number is: ', end='.')
        for number in allNumber:
            print(number, end=" ")
        
        print(f'\nThe minimum number from your input is {minNum}.')
        print(f'The maximum number from your input is {maxNum}.')
    
def checkOdd():
    allNumber = []
    oddNumber = []
    
    while True:
        theNumber = input('Input your number (fill blank to close): ')
        if theNumber != '':
            theNumber = int(theNumber)
            if theNumber % 2 != 0:
                oddNumber.append(theNumber)
            allNumber.append(theNumber)
        else:
            break
        
    print('All your inputted number is: ', end="")
    for i in range(0, len(allNumber)):
        print(allNumber[i], end=" ")
    
    print('\nAll your Odd number is: ', end="")
    for i in range(0, len(oddNumber)):
        print(oddNumber[i], end=" ")

def checkMax():
    allNumber = []

    firstNum = input('Input Your number (fill blank to close): ')
    
    
    
# def averageNumber():
    
    
# def primeCheck():
    
    
# def factorial():


# def subtraction():


# def divine():


# def multiply():
    
action = int(input('1. Summation\n2. Check Min n Max number\n3. Check the Odd number\n4. Check the Max number\n5. Check Average spawn number\n6. Check prime nunmber\n7. Factorial count\n8. Number Subtraction\n9. Divine Number\n10. Multiply Number\nChoose your action: '))
match action:
    case 1:
        summation()
    case 2:
        minMax()
    case 3:
        checkOdd()
    case 4:
        checkMax()
    case 5:
        averageNumber()
    case 6:
        primeCheck()
    case 7:
        factorial()
    case 8:
        subtraction()
    case 9:
        divine()
    case 10:
        multiply()