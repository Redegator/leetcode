def reverse(x: int) -> int:

    if x == 0:
        res = 0

    else:
        res = str(x)[::-1]

        while res[-1] == "0":
            res = res[:-1]

        if x<0:
            res = "-" + res[:-1]

        res = int(res)
        if res >= (2**31)-1 or res <= -2**31:
            res = 0

    return res


print(reverse(0))