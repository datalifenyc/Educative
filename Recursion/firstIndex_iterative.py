def firstIndex(arr, testVariable, currentIndex):
    # Write your code here
    for i in range(len(arr)):
        if arr[i] == testVariable:
            return i

    return -1


arr = [9, 8, 1, 8, 1, 7]
targetNumber = 1
currentIndex = 0
print(firstIndex(arr, targetNumber, currentIndex))
