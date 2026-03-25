stack_top = []
pairs = {
    ")": "(",
    "]": "["
}

while True:
    stack = input("Input here (fill blank to close): ")
    if stack == "()" and stack == "[]":
        stack_top.append(stack)
    else:
        print("this is not a brackets.")

    char = len(stack_top)

    if pairs[char] == stack_top:
        print(pairs[char])
    else:
        print("Error.")