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


def two_sum_multiple(nums, target):
    Map = {}
    res = []
    
    for i, val in enumerate(nums):
        comp = target - val
        if comp in Map:
            for prev in Map[comp]:
                if prev in prev:
                    res.append([prev, i])
        
        if val not in Map:
            Map[val] = []
        Map[val].append(i)
    return res if res else None

