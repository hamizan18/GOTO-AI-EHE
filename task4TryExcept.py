allNumber = []

while True:
    try:
        question = int(input('How much input do you want to make: '))
        break
    except:
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
    except:
        print('Just Input Number!!')

print('All Your number is: ', end="")
for i in range(0, len(allNumber)):
    print(allNumber[i], end=" ")