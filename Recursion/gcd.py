def gcd(testVariable1, testVariable2):
    # Write your code here
    if testVariable1 % testVariable2 == 0:
        return testVariable2

    if testVariable1 < testVariable2:
        return gcd(testVariable2, testVariable1)

    testVariable1 = testVariable1 % testVariable2
    return gcd(testVariable1, testVariable2)


print(gcd(14, 30))
