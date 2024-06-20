def searchInsert(nums, target) -> int:

    for pos in range(len(nums)):
        if target <= nums[pos]:
            res = pos
            break
        else:
            res = len(nums)

    return res


nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))