"""
用一个额外的数组来将每个元素放到正确的位置上，
也就是原本数组里下标为 i 的内容把它放到 (i+k)%数组长度 的位置。
然后把新的数组拷贝到原数组中。

复杂度分析



时间太长
"""

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    new_nums = nums.copy()
    nums_len = len(nums)
    if nums_len > 1:
        k = k % nums_len
        for i in range(nums_len):
            new_i = (i + k) % nums_len
            new_nums[new_i] = nums[i]
        nums = new_nums
    return nums


print(rotate([1, 2, 3, 4, 5], 3))
