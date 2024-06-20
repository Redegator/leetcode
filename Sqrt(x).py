def mySqrt(x: int) -> int:

    res = -1
    i = 0
    while res == -1:
        i += 1
        if i * i > x:
            res = i-1

    return res





x = 0
print(mySqrt(x))