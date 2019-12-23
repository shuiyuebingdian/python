def two_sum(nums, target):
    dct = {}
    for i, n in enumerate(nums):
        print("i=", i, " n=", n)
        if target - n in dct:
            return [dct[target - n], i]
        dct[n] = i


print(two_sum([14, 2, 31, 4], 6))
