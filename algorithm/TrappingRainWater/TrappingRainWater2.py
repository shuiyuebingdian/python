"""
时间复杂度O(n)
空间复杂度O(n)
"""


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    amount = 0
    length = len(height)
    max_left = 0
    # 每一列右边的最高值数组
    max_right = [0] * length

    for i in range(length - 2, 0, -1):
        # 第i列右边的最大值是： 第i+1列右边最高的值 和 第i+1列的值 中的最大值
        max_right[i] = max(height[i + 1], max_right[i + 1])

    for i in range(1, length - 1):
        # 找出左边最高墙的高度
        if max_left < height[i - 1]:
            max_left = height[i - 1]
        # 当前墙的高度
        current = height[i]
        # 找出最小值
        min_height = min(max_left, max_right[i])
        if current < min_height:
            amount += min_height - current
    return amount


print(trap([2, 0, 2]))
