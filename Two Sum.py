def twoSum(nums, target: int) -> [int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                res = [j, i]

    return res





nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))