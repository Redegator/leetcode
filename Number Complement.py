def findComplement(num):
    binary = str(bin(num))[2:]

    res = ""
    for element in binary:
        if element == "1":
            res += "0"
        else: res += "1"

    return int(res, 2)


print(findComplement(5))
