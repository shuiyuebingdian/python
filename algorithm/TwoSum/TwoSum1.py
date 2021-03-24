
def two_sum(nums, target):

    target_list = []
    for i in range(len(nums) - 1):
        a = nums[i]
        for j in range(i + 1, len(nums)):
            b = nums[j]
            if a + b == target:
                target_list.append(i)
                target_list.append(j)
                return target_list


class Solution:
    pass
