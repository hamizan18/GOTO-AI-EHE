# MUTABLE
data = [[1], [2], [3]]

for x in data:
    x.append(99)

for x in data:
    print(x, end=" ")
    

# IMMUTABLE
data = [10, 20, 30]

for x in data:
    x.append(5)

for x in data:
    print(x, end=" ")