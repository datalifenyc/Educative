def merge_lists(lst1, lst2):
    complete_list = []
    i = 0
    j = 0
    total_length = len(lst1) + len(lst2)

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            complete_list.append(lst1[i])
            i+=1
        else:
            complete_list.append(lst2[j])
            j+=1

    while i < len(lst1):
        complete_list.append(lst1[i])
        i+=1

    while j < len(lst2):
        complete_list.append(lst2[j])
        j+=1
    
    return complete_list

print(merge_lists([1,2,3], [1,2,3]))
    