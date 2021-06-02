def max_min(lst):
    result = []
    # iterate half list
    for i in range(len(lst)//2):
        # Append corresponding last element
        result.append(lst[-(i+1)])
        # append current element
        result.append(lst[i])
    if len(lst) % 2 == 1:
        # if middle value then append
        result.append(lst[len(lst)//2])
    return result


print(max_min([1, 2, 3, 4, 5, 6]))
