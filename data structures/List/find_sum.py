def find_sum(lst, k):

    l = 1
    for i in lst:
        for j in range(l, len(lst)):
            if i + lst[j] == k:
                return [i, lst[j]] 
        l+=1



lst = [1,21,3,14,5,60,7,6]
k = 81

print(find_sum(lst, k))