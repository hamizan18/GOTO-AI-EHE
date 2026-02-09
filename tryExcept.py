allNumber = []
def inputter():
    firstNumber = input('Input Your number here: ')
    return firstNumber

while number == None:
    try:
        number = int(inputter())
    except:
        print("Error, this isn't number!")
        inputter()
    
print(f'Your number is: {number}')