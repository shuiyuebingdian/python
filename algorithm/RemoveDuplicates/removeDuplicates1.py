
def remove_duplicates(nums):
    nums_len = len(nums)
    if nums_len == 0:
        return 0
    else:
        i = 0
        for j in range(1, nums_len):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
