angka = []
n = int(input("Enter number of inputs: "))

for i in range(0, n):
    number = int(input(f"Enter number [{i+1}]: "))
    angka.append(number)
    average = angka[i] / n

print("\nYour input numbers are: ")
for i in range(0, n):
    print(f'{angka[i]}', end=", ")
    
print(f'\nThe average number from your input is: {average}')