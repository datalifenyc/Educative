from Stack import MyStack


def evaluate_post_fix(exp):
    s = MyStack()
    for i in exp:
        if i == " ":
            continue
        elif i == "+":
            first_value = s.pop()
            second_value = s.pop()
            s.push(int(second_value) + int(first_value))
        elif i == "-":
            first_value = s.pop()
            second_value = s.pop()
            s.push(int(second_value) - int(first_value))
        elif i == "/":
            first_value = s.pop()
            second_value = s.pop()
            s.push(int(second_value) / int(first_value))
        elif i == '*':
            first_value = s.pop()
            second_value = s.pop()
            s.push(int(second_value) * int(first_value))
        else:
            s.push(i)

    return s.top()


exp = "921 * - 8 - 4 +"

print(evaluate_post_fix(exp))
