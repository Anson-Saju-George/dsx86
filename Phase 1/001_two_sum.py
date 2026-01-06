# Two Sum Problem Solutions
"""
This module provides three different implementations to solve the Two Sum problem:
    1. Finding a single pair of indices that sum to the target.
    2. Finding all pairs of indices that sum to the target, including duplicates.
    3. Finding all unique pairs of values that sum to the target, avoiding duplicates.
"""

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


"""
    To be studies later: Uses sliding window / two-pointer technique after sorting the array.
"""


def two_sum_unique(nums, target):
    nums.sort()  # Sort the array to use two-pointer technique
    res = []  # Result list for unique pairs
    l, r = 0, len(nums) - 1  # Initialize two pointers
    while l < r:  # While left pointer is less than right pointer
        s = nums[l] + nums[r]  # Calculate the sum of values at both pointers
        if s == target:  # If sum matches target
            res.append([nums[l], nums[r]])  # Append the pair to result
            l += 1  # Move left pointer to the right
            r -= 1  # Move right pointer to the left
            while l < r and nums[l] == nums[l - 1]:  # Skip duplicates for left pointer
                l += 1
            while l < r and nums[r] == nums[r + 1]:  # Skip duplicates for right pointer
                r -= 1
        elif s < target:  # If sum is less than target, move left pointer to the right
            l += 1
        else:  # If sum is greater than target, move right pointer to the left
            r -= 1
    return res  # Return the list of unique pairs


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
