"""
先反转前 k 个元素，再反转后面 n-kn−k 个元素，最后反转所有元素
"""


def reverse(nums, start, end):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    nums_len = len(nums)
    k = k % nums_len
    # 翻转前半部分
    reverse(nums, 0, nums_len - k - 1)
    # 翻转后半部分
    reverse(nums, nums_len - k, nums_len - 1)
    nums.reverse()


print(rotate([1, 2, 3, 4, 5], 3))
