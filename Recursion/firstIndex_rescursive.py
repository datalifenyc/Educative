def firstIndex(arr, testVariable, currentIndex):
    # Write your code here
    if currentIndex == len(arr):
        return -1

    if testVariable == arr[currentIndex]:
        return currentIndex

    return firstIndex(arr, testVariable, currentIndex + 1)


arr = [9, 8, 1, 8, 1, 7]
targetNumber = 1
currentIndex = 0
print(firstIndex(arr, targetNumber, currentIndex))
