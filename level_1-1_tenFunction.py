def summation():
    res = 0
    max = int(input('Input max input number: '))
    
    for i in range(0, len(max)):
        sum = input(f'Number-{i}: ')
        res += sum
    
def minMax():
    allNumber = []
    maxNum = 0
    minNum = 0
    
    n = int(input('Input Your number: '))
    allNumber.append(n)
    
    if n > maxNum:
        maxNum = n
    if n < minNum:
        minNum = n
    
    print('All Your inputted number is: ')
    for i in range(0, len(allNumber)):
        print(allNumber[i], end=" ")
    
def checkOdd():
    
    
def checkMax():
    
    
def averageNumber():
    
    
def primeCheck():
    
    
def factorial():


def subtraction():


def divine():


def multiply():
    
summation()
minMax()
checkOdd()
checkMax()
averageNumber()
primeCheck()
factorial()
subtraction()
divine()
multiply()