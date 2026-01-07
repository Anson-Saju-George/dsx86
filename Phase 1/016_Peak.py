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


def find_all_peaks(nums):
    n = len(nums)
    peaks = []

    for i in range(n):
        left  = nums[i-1] if i > 0 else float('-inf')
        right = nums[i+1] if i < n-1 else float('-inf')

        if nums[i] > left and nums[i] > right:
            peaks.append(i)

    return peaks


# Example usage:
nums = [1, 5, 3, 4, 1]
print(find_peak(nums))
nums = [0, 1, 0, 2, 1]
print(find_peak(nums))
nums = [3, 2, 1] + [1, 2, 3,]
print(find_peak(nums))

nums = [1, 5, 3, 4, 1, 7, 6] # Indices [1,3,5] are peaks
print(find_all_peaks(nums))