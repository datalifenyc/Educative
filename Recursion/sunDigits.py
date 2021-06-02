def sumDigits(testVariable):
    # Write your code here
    if len(testVariable) == 1:
        return int(testVariable[0])
    return int(testVariable[0]) + sumDigits(testVariable[1:])


print(sumDigits("345"))
