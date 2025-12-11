def kadane(nums):
    max_sum = nums[0]
    curr = nums[0]

    for x in nums[1:]:
        curr = max(x, curr + x)
        max_sum = max(max_sum, curr)

    return max_sum


def max_circular_subarray(nums):
    if not nums:
        return 0

    # standard max subarray
    max_kad = kadane(nums)

    # if all negative, kadane already gives the max (largest negative)
    if max_kad < 0:
        return max_kad

    total = sum(nums)

    # find min subarray via inverted-kadane trick
    inv_curr = inv_max = -nums[0]
    for x in nums[1:]:
        inv_curr = max(-x, inv_curr + -x)
        inv_max = max(inv_max, inv_curr)
    # inv_max is max of inverted array => -min_subarray_sum
    min_subarray_sum = -inv_max

    # max wrap sum:
    wrap_sum = total - min_subarray_sum

    return max(max_kad, wrap_sum)
