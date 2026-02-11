def inputter():
    firstNumber = input('Input Your number here: ')
    return firstNumber

while True:
    try:
        number = int(inputter())
        break
    except:
        print("Error, this isn't number!")

print(f'Your number is: {number}')