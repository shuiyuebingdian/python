"""
最简单的方法是旋转 k 次，每次将数组旋转 1 个元素
复杂度分析

时间复杂度：O(n*k)
空间复杂度：O(1)

时间太长
"""

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nums_len = len(nums)
    if nums_len > 1:
        k = k % nums_len
        for i in range(k):
            previous = nums[nums_len - 1]
            for j in range(nums_len):
                temp = nums[j]
                nums[j] = previous
                previous = temp
    return nums


print(rotate([1, 2, 3, 4, 5], 3))
