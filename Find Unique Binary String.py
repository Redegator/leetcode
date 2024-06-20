def findDifferentBinaryString(nums) -> str:

    n = len(nums[0])
    existing_nums = ["0", "1"]


    for i in range(n-1):
        new_list = []
        for x in existing_nums:
            new_list.append(x + "1")
            new_list.append(x + "0")

            existing_nums = new_list


    for unique in existing_nums:
        if unique not in nums:
            res = unique
            break

    return res


nums = ["111","011","001"]
print(findDifferentBinaryString(nums))