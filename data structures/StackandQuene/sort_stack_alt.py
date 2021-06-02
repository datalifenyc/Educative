from Stack import MyStack
"""
1. Use a second temp_stack.
2. Pop value from main_stack.
3. If the value is greater or equal to the top of temp_stack,
  then push the value in temp_stack
  else pop all values from temp_stack
      and push them in main_stack
      and in the end push value in temp_stack
4.repeat from step 2 till main_stack is not empty.
5. When main_stack will be empty,
    temp_stack will have sorted values in descending order.
6. Now transfer values from temp_stack to main_stack
    to make values sorted in ascending order.
"""


def sort_stack(stack):

    temp_stack = MyStack()

    while stack.is_empty() is False:

        value = stack.pop()

        if temp_stack.top() is not None and value >= int(temp_stack.top()):
            # if value is not none and larger, push it at the top of temp_stack
            temp_stack.push(value)
        else:
            while temp_stack.is_empty() is False:
                stack.push(temp_stack.pop())
            # place value as the smallest element in temp_stack
            temp_stack.push(value)

    # Transfer from temp_stack => stack
    while temp_stack.is_empty() is False:
        stack.push(temp_stack.pop())

    return stack


stack = MyStack()
stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)

sort_stack(stack)

# Printing by popping
print([stack.pop() for i in range(stack.size())])
