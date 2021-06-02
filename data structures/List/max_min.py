def max_min(lst):
    i = 0
    new_list = []
    while i < len(lst)//2:
        last_element = lst.pop()
        new_list.append(last_element)
        if i < len(lst):  
            new_list.append(lst[i])
        i+=1
    return new_list

lst = [1,2,3,4,5]

print(max_min(lst))