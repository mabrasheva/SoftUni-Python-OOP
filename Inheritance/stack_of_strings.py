class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


data_stack = Stack()
data_stack.push("element1")
data_stack.push("element2")
data_stack.push("element3")
data_stack.push("element4")
print(data_stack)
print(data_stack.pop())
print(data_stack.top())
print(data_stack.is_empty())
print(data_stack.__str__())
