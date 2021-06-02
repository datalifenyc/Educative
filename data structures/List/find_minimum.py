def find_minimum(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum
    
print(find_minimum([9,2,3,6]))