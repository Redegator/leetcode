def threeSum(nums):

    result = []
    result_final = []

    for i in nums:
        nums_without_i = nums.copy()
        nums_without_i.remove(i)
        for j in nums_without_i:
            nums_without_ij = nums_without_i.copy()
            nums_without_ij.remove(j)
            for k in nums_without_ij:
                if i + j + k == 0:

                    x = [i,j,k]
                    x.sort()
                    result.append(x)

    for element in result:
        if result_final.count(element) == 0:
            result_final.append(element)
    return result_final



nums = [-1,0,1,2,-1,-4]
# nums = [11,-8,9,-6,-10,14,-5,-10,2,-1,-14,-13,-5,9,-5,-12,9,5,-1,-4,-14,5,-11,3,6,-7,2,-14,9,-6,-8,-2,-7,8,7,-2,7,9,3,-14,-14,5,-12,-4,-9,-1,-8,7,11,-2,-11,4,-11,-15,-7,10,-7,10,4,10,11,11,-7,-11,4,7,2,-12,1,12,-10,2,2,-15,6,1,-1,13,-7,-12,-4,-11,7,0,-11,-15,-12,-10,2,7,-15,-2,3,-15,-6,14,-1,11,-13,-15,9,14,-5,-12,-15,-14,4,-9,6,5,-6,-13,9]
print(threeSum(nums))
