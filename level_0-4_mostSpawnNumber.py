numb = []

addNumb = 'Y'

while addNumb != 'X':
    addNumb = input("Input your number (klik 'X' or fill blank to print): ")
    if addNumb == 'X' or addNumb == '':
        break
    
    if addNumb == int(addNumb):
        numb.append(addNumb)
    
for i in range(0, len(numb)):
    print(numb[i], end=" ")