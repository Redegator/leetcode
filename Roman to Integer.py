def romanToInt(self, s: str) -> int:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "z": 0
    }
    res = 0
    s += "z"

    for i in range(len(s) - 1):
        n = s[i]

        if symbols.get(n) >= symbols.get(s[i + 1]):
            res += symbols.get(n)

        elif symbols.get(n) < symbols.get(s[i + 1]):
            res -= symbols.get(n)

    return res