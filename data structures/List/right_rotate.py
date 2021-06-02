def right_rotate(lst, n):
    info = {}
    new_list = []

    for i in range(len(lst)):
        info[(i+3)%5] = lst[i]

    for i in range(len(lst)):
        new_list.append(info[i])

    return new_list


lst = []
n = 3

print(right_rotate(lst, n))