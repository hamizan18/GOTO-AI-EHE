def inputter():
    number = input('Input Your number (1 - 100): ')
    return number

while True:
    try:
        theNumber = int(inputter())
        if 1 <= theNumber <= 100: break
        else:
            print('Error, You must be input number between 1 and 100')
    except ValueError:
        print('Error, please just input a number')
        
print(f'Your number is: {theNumber}')