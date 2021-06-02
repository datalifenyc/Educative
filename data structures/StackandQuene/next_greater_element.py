from Stack import MyStack


def next_greater_element(lst):
    # Write your code here
    result = []
    s = MyStack()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                s.push(lst[j])
                break
        if lst[i] == s.top():
            s.push(-1)
            result.append(s.top())
        else:
            result.append(s.top())
    return result


lst = [4, 6, 3, 2, 8, 1]
print(next_greater_element(lst))
