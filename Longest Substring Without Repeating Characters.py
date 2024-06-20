def lengthOfLongestSubstring(s: str) -> int:

    res = 0
    for i in range(len(s)):
        for j in range(len(s)-i+1):
            test = s[i:i+j]

            if len(set(test)) == j and len(test) > res:
                res = j

    return res





s = "pwwkew"
print(lengthOfLongestSubstring(s))