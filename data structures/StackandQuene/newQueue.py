from Stack import MyStack
# We can use 2 stacks for this purpose,main_stack to store original values
# and temp_stack which will help in enqueue operation.
# Main thing is to put first entered element at the top of main_stack


class NewQueue:
    def __init__(self):
        # Can use size from argument to create stack
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

        # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        self.main_stack.push(value)
        print(str(value) + " enqueued")
        return True

        # Removes Element From Queue

    def dequeue(self):
        # If both stacks are empty, end operation
        if self.temp_stack.is_empty():
            if self.main_stack.is_empty():
                return None
            # Transfer all elements to temp_stack
            while self.main_stack.is_empty() == False:
                value = self.main_stack.pop()
                self.temp_stack.push(value)
        # Pop the first value. This is the oldest element in the queue
        temp = self.temp_stack.pop()
        print(str(temp) + " dequeued")
        return temp


queue = NewQueue()
for i in range(5):
    queue.enqueue(i+1)

print("----------")

for i in range(5):
    queue.dequeue()
