'''
Insertion Sort
插入排序
'''

class Solution:
    def twoSum(nums, target) :
        targetList = []
        find = False
        for i in range(len(nums) - 1):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if a + b == target:
                    targetList.append(i)
                    targetList.append(j)
                    return targetList
                
    
    if __name__ == "__main__":
        nums = [2, 3, 7, 11, 15]
        target = 9
        print(twoSum(nums, target))
