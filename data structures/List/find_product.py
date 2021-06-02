import math

def find_product(lst):
    product_list = []
    total = 1

    for i in lst:
        total *= i
    
    i = 0
    if total == 0:
        total = 1
        while i < len(lst):
            if lst[i] == 0:
                continue
            else:
                total *= lst[i]
        
        for i in range(len(lst)):
            if lst[i] == 0:
                product_list.append(total)
            else:
                product_list.append(0)
        return product_list

    for i in range(len(lst)):
        product_list.append(math.floor(total/lst[i]))
    return product_list
        

arr = [1,2,3,4]

print(find_product(arr))