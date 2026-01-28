print("Enter a number:")
number1 = int(input('Enter number 1 : '))
for i in range(2, 6):
    number = int(input(f'Enter number {i} : '))
    if number > number1:
        number1 = number

print(f'\nThe largest number from your 5 input is: {number1}')

