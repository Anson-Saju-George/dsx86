def find_peak(nums):
    """
    Returns index of any peak element (nums[i] > nums[i-1] and nums[i] > nums[i+1]),
    with edges treated as having -inf neighbors.
    """
    n = len(nums)
    if n == 0:
        return -1
    if n == 1:
        return 0

    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        # if ascending slope, peak is to the right
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    # lo == hi is a peak index
    return lo

nums = [1, 2, 3, 1]
print(find_peak(nums))
nums = [0, 1, 0, 2, 1]
print(find_peak(nums))
nums = [3, 2, 1] + [1, 2, 3,]
print(find_peak(nums))