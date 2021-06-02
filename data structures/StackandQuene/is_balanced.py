from Stack import MyStack


def is_balanced(exp):
    s = MyStack()
    for i in exp:
        if i == "{" or i == "[" or i == "(":
            s.push(i)
        if i == "}":
            if s.top() == "{":
                s.pop()
            else:
                return False
        if i == "]":
            if s.top() == "[":
                s.pop()
            else:
                return False
        if i == ")":
            if s.top() == "(":
                s.pop()
            else:
                return False

    return True


exp = "{[({})]}("
print(is_balanced(exp))
