def longestCommonPrefix(self, strs: List[str]) -> str:
    length = []
    for string in strs:
        length.append(len(string))

    short = min(length)

    res = ""
    count = 0
    for i in range(short):
        is_unique = []
        for string in strs:
            is_unique.append(string[0:i + 1])

        is_unique = set(is_unique)
        if len(is_unique) == 1 or len(strs) == 1:
            count = i + 1
            res = strs[0][0:count]

    return res