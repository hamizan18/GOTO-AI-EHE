def inputAngka():
    while True:
        try:
            number = int(input('Input Your Number : '))
            break
        except:
            print('Please just input number.')
    
    return number

angka = inputAngka()

print(f'Your number is: {angka}')