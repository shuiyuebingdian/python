"""
时间最优

思路：
将和为目标值的那 两个 整数定义为 num1 和 num2
创建一个新字典，内容存在数组中的数字及索引
将数组nums转换为字典，
遍历字典， num1为字典中的元素（其实与数组总的元素一样），
num2 为 target减去num1， 判定num2是否在字典中，如果存在，返回字典中num2的值（也就是在数组nums中的下标）和 i（也就是num1在数组中的下标）
如果不存在，设置字典num1的值为i
"""

def two_sum(nums, target):
    dct = {}
    for i, num1 in enumerate(nums):
        num2 = target - num1
        if num2 in dct:
            return [dct[num2], i]
        dct[num1] = i


print(two_sum([14, 2, 31, 4], 6))
