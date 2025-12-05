def two_sum_single(nums, target):
    mp = {}   # val -> index
    for i, val in enumerate(nums):
        comp = target - val
        if comp in mp:
            return [mp[comp], i]
        mp[val] = i
    return None

def two_sum_multiple(nums, target):
    mp = {}       # val -> list of indices
    res = []      # result pairs
    for i, val in enumerate(nums):
        comp = target - val
        # if complement is seen before
        if comp in mp:
            for prev_index in mp[comp]:
                res.append([prev_index, i])
        # store this val's index
        if val not in mp:
            mp[val] = []
        mp[val].append(i)
    return res if res else None


nums = [2, 7, 11, 15]
print(two_sum_single(nums, 10))
print(two_sum_multiple(nums, 10))

