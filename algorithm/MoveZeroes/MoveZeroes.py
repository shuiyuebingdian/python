#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
#输出: [1,3,12,0,0]
#
# 说明:
#
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
# Related Topics 数组 双指针

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    non_zero_index = 0
    length = len(nums)
    for i in range(length):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    while non_zero_index < length:
        nums[non_zero_index] = 0
        non_zero_index += 1
    return nums


print(moveZeroes([0, 2, 2, 0]))
