numb = []

addNumb = 'Y'

while addNumb != 'X':
    addNumb = input("Input your number (klik 'X' or fill blank to print): ")
    if addNumb == 'X' or addNumb == '':
        break
    
    if addNumb:
        numb.append(addNumb)
    
for i in range(0, len(numb)):
    if numb[i] == str:
        numb[i] = ''
    print(numb[i], end=" ")