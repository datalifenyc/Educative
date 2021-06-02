def recursiveLength(testVariable):
    # Write your code here
    if testVariable == "":
        return 0
    return 1 + recursiveLength(testVariable[1:])


print(recursiveLength("act"))
