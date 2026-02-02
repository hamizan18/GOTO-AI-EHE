action = input('Choose your action:\n1. Summation\n2. Check Min n Max number\n3. Check the Odd number\n4. Check the Max number\n5. Check Average spawn number\n6. Check prime nunmber\n7. Factorial count\n8. Number Subtraction\n9. Divine Number\n10. Multiply Number')
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
        
# FUNCTION
def summation():
    res = 0
    max = int(input('Input max input number: '))
    
    for i in range(0, max):
        sum = int(input(f'Number-{i+1}: '))
        res = int(res + sum)
    
    print(f'The summation from your input is: {res}')
    
def minMax():
    allNumber = []
    maxNum = 0
    minNum = 0
    
    while True:
        n = input('Input Your number (fill blank to close): ')
        if n != '':
            n = int(n)
            allNumber.append(n)
        if n == '':
            break
        
        if n > maxNum:
            maxNum = n
        if n < minNum:
            minNum = n
    
    print('All Your inputted number is: ', end='')
    for i in range(0, len(allNumber)):
        print(allNumber[i], end=" ")
    
def checkOdd():
    allNumber = []
    oddNumber = []
    
    while True:
        theNumber = input('Input your number (fill blank to close): ')
        if theNumber != '':
            theNumber = int(theNumber)
            if theNumber % 2 == 0:
                oddNumber.append(theNumber)
            allNumber.append(theNumber)
        if theNumber == '':
            break
        
    print('All your inputted number is: ', end="")
    for i in range(0, len(allNumber)):
        print(allNumber[i], end=" ")
    
    print('\nAll your Odd number is: ', end="")
    for i in range(0, len(oddNumber)):
        print(oddNumber[i], end=" ")

# def checkMax():
    
    
# def averageNumber():
    
    
# def primeCheck():
    
    
# def factorial():


# def subtraction():


# def divine():


# def multiply():
    