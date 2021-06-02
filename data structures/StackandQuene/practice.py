class MyStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


stack = MyStack()
for i in range(10):
    stack.push(i)

print(print(f'top: {str(stack.top())}'))

for x in range(5):
    print(f'pop: {str(stack.pop())}')


print("is_empty(): " + str(stack.is_empty()))  # Checking if its empty
