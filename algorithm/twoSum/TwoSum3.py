"""
思路：

"""


def two_sum(nums, target):
    nums_len = len(nums)
    for i in range(nums_len):
        num1 = nums[i]
        num2 = target - num1
        if i < nums_len - 1 and num2 in nums[i + 1:]:
            return [i, nums.index(num2, i + 1)]


print(two_sum([2, 7, 11, 15], 9))
