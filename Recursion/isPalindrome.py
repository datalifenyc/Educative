def isPalindrome(testVariable):
    # Write your code here
    if len(testVariable) <= 1:
        return True
    if testVariable[0] != testVariable[-1]:
        return False

    return isPalindrome(testVariable[1:-1])


print(isPalindrome("madam"))
