def rearrange(lst):
    neg_lst = []
    pos_lst = []
    final_lst = []

    for i in lst:
        if i < 0:
            neg_lst.append(i)
    for i in lst:
        if i >= 0:
            pos_lst.append(i)

    final_lst = neg_lst + pos_lst

    return final_lst

    
print(rearrange([10,-1,20,4,5,-9,-6]))