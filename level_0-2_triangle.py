n = int(input("Enter a number: "))
# n = 5

for i in range(n, 0, -1):
    print(i * " " + "* " * (n + 1 - i))