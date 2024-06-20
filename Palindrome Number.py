def isPalindrome(x: int) -> bool:

    x = str(x)
    res = True
    for i in range(len(x)):
        if x[i] != x[-i-1]:
            res = False


    return res





x = 1211212
print(isPalindrome(x))