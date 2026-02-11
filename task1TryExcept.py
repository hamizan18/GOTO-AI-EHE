def inputter():
    number = input('Input Your number here: ')
    return number

while True:
    try:
        theNumber = int(inputter())
        break
    except ValueError:
        print('Error, you can just input number!')

print(f'Your number is: {theNumber}')