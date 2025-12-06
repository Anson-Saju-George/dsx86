def two_sum_single(nums, target):
    mp = {}  # Value to Index mapping
    for i, val in enumerate(nums):  # Iterate with index and value
        comp = target - val  # Compute complement
        if comp in mp:  # Check if complement exists
            return [mp[comp], i]  # Return indices if found
        mp[val] = i  # Store value and index
    return None


def two_sum_multiple(nums, target):
    mp = {}  # Value to Indices mapping
    res = []  # Result list for pairs

    for i, val in enumerate(nums):  # Iterate with index and value
        comp = target - val  # Compute complement

        if comp in mp:  # Check if complement exists with all previous indices in map
            for prev_index in mp[comp]:  # Iterate through all indices of the complement
                res.append([prev_index, i])  # Append the pair

        if val not in mp:  # Initialize list if value not in map
            mp[val] = []  # Create a new list for this value
        mp[val].append(i)  # Append current index to the list for this value

    return res if res else None


def two_sum_unique(nums, target):
    nums.sort()
    res = []
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            res.append([nums[l], nums[r]])
            l += 1
            r -= 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
            while l < r and nums[r] == nums[r + 1]:
                r -= 1
        elif s < target:
            l += 1
        else:
            r -= 1
    return res


nums = [2, 7, 11, 15, 8, 1]
print("Single pair:")
print(two_sum_single(nums, 9))
print()

print("Multiple pairs:")
print(two_sum_multiple(nums, 9))
print()

print("Unique pairs:")
print(two_sum_unique([1, 3, 2, 2, 3, 1], 4))
print(two_sum_unique([1, 2, 3, 4, 5], 6))
print(two_sum_unique([1, 1, 1, 1], 2))
