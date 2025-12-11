def exists_subarray_sum_k(nums, k):
    prefix = 0
    seen = {0}

    for x in nums:
        prefix += x
        if (prefix - k) in seen:
            return True
        seen.add(prefix)
    return False


