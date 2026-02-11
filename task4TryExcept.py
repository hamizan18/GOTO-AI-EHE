allNumber = []

while True:
    try:
        question = int(input('Please input a positive number that greater than 0: '))
        if question > 0:
            break
        else:
            print('Do not input negative number!')
    except ValueError:
        print('Number only!')

i = 0
while i < question:
    try:
        number = int(input('Input Your Number(must be a positive number): '))
        if number >= 0:
            allNumber.append(number)
            i+=1
        else:
            print("Do not input negative number!")
    except ValueError:
        print('Just Input Number!!')

print('All Your number is: ', end="")
for number in allNumber:
    print(number, end=" ")