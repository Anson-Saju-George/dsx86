def count_subarrays_div_by_k(nums, k):
    freq = {0: 1}        # prefix 0 seen once
    prefix = 0
    count = 0

    for x in nums:
        prefix += x
        mod = prefix % k
        # normalize negative mods (Python % already non-negative, but keep for clarity)
        if mod < 0:
            mod += k

        count += freq.get(mod, 0)
        freq[mod] = freq.get(mod, 0) + 1

    return count



