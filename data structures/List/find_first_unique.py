def find_first_unique(lst):
    # Write your code here
    left = []
    while len(lst) !=  1:
        i = 1
        if lst[0] not in lst[1:]:
            return lst[0]
        while i < len(lst):
            if lst[i] == lst[0]:
                lst.pop(0)
                lst.pop(i-1)
            i+=1
    return lst[0]


print(find_first_unique([3,2,3,2,6,6,4]))