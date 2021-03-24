"""
时间复杂度O(n²)
空间复杂度O(1)
"""


def get_max_height(height, start, end):
    max_height = 0
    for i in range(start, end):
        if height[i] > max_height:
            max_height = height[i]
    return max_height


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    amount = 0
    length = len(height)
    for i in range(1, length - 1):
        # 找出左边最高墙的高度（从第0位到i前面一位）
        max_left = get_max_height(height, 0, i)
        # 找出后边最高墙的高度(从i后面一位，到最后一位)
        max_right = get_max_height(height, i + 1, length)
        # 当前墙的高度
        current = height[i]
        # 找出最小值
        min_height = min(max_left, max_right)
        if current < min_height:
            amount += min_height - current
    return amount


print(trap([2, 0, 2]))
