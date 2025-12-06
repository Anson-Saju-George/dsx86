def two_sum(nums, target):
    Map = {}

    for i, val in enumerate(nums):
        comp = target - val
        if comp in Map:
            return [Map[comp], i]
        Map[val] = i

nums = [1, 2, 3, 4, 5]
target = 9
print(two_sum(nums, target))