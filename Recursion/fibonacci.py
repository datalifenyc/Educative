def fibonacci(testVariable):
    if testVariable == 0:
        return 0
    if testVariable == 1:
        return 1
    if testVariable == 2:
        return 1
    return fibonacci(testVariable - 1) + fibonacci(testVariable - 2)


n = 7
print(fibonacci(n))
