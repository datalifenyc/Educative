class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack1 = []
        self.stack2 = []

    # Insert Value in First Stack
    def push1(self, value):
        self.stack1.append(value)

    # Insert Value in Second Stack
    def push2(self, value):
        self.stack2.append(value)

    # Return and remove top Value from First Stack
    def pop1(self):
        return self.stack1.pop()

    # Return and remove top Value from Second Stack
    def pop2(self):
        return self.stack2.pop()
