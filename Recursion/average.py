def average(testVariable, currentIndex=0):
    if not testVariable:
        return None
    if len(testVariable) == 1:
        return testVariable[0]

    if len(testVariable) > 1 and currentIndex < len(testVariable)-1:
        testVariable[currentIndex+1] = testVariable[currentIndex] + \
            testVariable[currentIndex+1]
        return average(testVariable, currentIndex+1)
    if currentIndex == len(testVariable)-1:
        return testVariable[currentIndex]/(currentIndex+1)


testVariable = [10, 2, 3, 4, 8, 0]
currentIndex = 0

print(average(testVariable, currentIndex))
