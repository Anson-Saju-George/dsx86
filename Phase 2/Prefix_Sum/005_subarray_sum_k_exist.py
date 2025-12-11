def exists_subarray_sum_k(nums, k):
    prefix = 0
    seen = {0}

    for x in nums:
        prefix += x
        if (prefix - k) in seen:
            return True
        seen.add(prefix)
    return False


# Example usage:
nums = [1, 2, 3, 4, 5]
k = 9
print(exists_subarray_sum_k(nums, k))  # Output: True
