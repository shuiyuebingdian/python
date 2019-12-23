"""
用一个额外的数组来将每个元素放到正确的位置上，
也就是原本数组里下标为 i 的内容把它放到 (i+k)%数组长度 的位置。
然后把新的数组拷贝到原数组中。

复杂度分析



时间太长
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
