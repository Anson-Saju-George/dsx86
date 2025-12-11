def longest_zero_sum(nums):
    prefix = 0
    pos = {0: -1}
    longest = 0

    for i, x in enumerate(nums):
        prefix += x
        if prefix in pos:
            longest = max(longest, i - pos[prefix])
        else:
            pos[prefix] = i

    return longest


nums = [1, -1, 3, 2, -2, -3, 3]
nums2 = [2, -2, 3, -3, 4, -4, 1]

print(longest_zero_sum(nums))
print(longest_zero_sum(nums2))