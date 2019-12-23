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
    k = k % len(nums)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums) - 1)
    nums.reverse()
    return nums


print(rotate([1, 2, 3, 4, 5], 3))
