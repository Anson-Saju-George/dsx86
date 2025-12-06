def two_sum_single(nums, target):
    mp = {} # Value to Index mapping
    for i, val in enumerate(nums): # Iterate with index and value
        comp = target - val # Compute complement
        if comp in mp: # Check if complement exists
            return [mp[comp], i] # Return indices if found
        mp[val] = i # Store value and index
    return None

def two_sum_multiple(nums, target):
    mp = {}  # Value to Indices mapping
    res = [] # Result list for pairs

    for i, val in enumerate(nums):  # Iterate with index and value
        comp = target - val         # Compute complement

        if comp in mp:              # Check if complement exists with all previous indices in map
            for prev_index in mp[comp]:  # Iterate through all indices of the complement
                res.append([prev_index, i])  # Append the pair

        if val not in mp:           # Initialize list if value not in map
            mp[val] = []            # Create a new list for this value
        mp[val].append(i)           # Append current index to the list for this value

    return res if res else None



nums = [2, 7, 11, 15, 8, 1]
print(two_sum_single(nums, 9))
print(two_sum_multiple(nums, 9))

