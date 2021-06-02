def decimalToBinary(testVariable):
    if testVariable == 0:
        return 0
    else:
        value = testVariable % 2 + 10 * decimalToBinary(testVariable//2)
    return value


print(decimalToBinary(10))
