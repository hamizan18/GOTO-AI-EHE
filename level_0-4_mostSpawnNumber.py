numb = []

addNumb = 'Y'

while addNumb != 'X' and addNumb != 'x':
    addNumb = input("Input your number (klik 'X' to close): ")

    if addNumb == 'X' and addNumb == 'x':
        break
    
    numb.append(int(addNumb))