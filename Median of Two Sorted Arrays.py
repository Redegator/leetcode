def findMedianSortedArrays(nums1, nums2) -> float:

    merged = nums1 + nums2
    merged = sorted(merged)

    n = len(merged)
    if n % 2 == 0:
        res = (merged[n//2] + merged[(n-1)//2]) / 2

    else:
        res = merged[n//2]

    return res





num1 = [1,2]
num2 = [2]

print(findMedianSortedArrays(num1, num2))