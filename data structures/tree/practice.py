def right_rotate(lst, k):
    lst_size = len(lst)
    new_lst = [0 for i in range(lst_size)]
    print(new_lst)
    for i in range(lst_size):
        print(f'\ni: {i}')
        if i <= k - 1:
            print(f'i + k: {i + k}')
            print(f'lst[i]: {lst[i]}')
            new_lst[i + k] = lst[i]
        else:
            print(f'i + (k * -1 + 1): {i + (k * -1 + 1)}')
            new_lst[i + (k * -1 + 1)] = lst[i]
        print(new_lst)
    return new_lst
