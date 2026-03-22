class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return "Stack kosong!"

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return "Stack kosong!"

    def is_empty(self):
        return len(self.data) == 0
    
    def show(self):
        return self.data
    
    
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.show())
print(s.pop())
print(s.peek())