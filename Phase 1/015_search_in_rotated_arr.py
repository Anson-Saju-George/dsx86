def search_rotated(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # left side sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # right side sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


nums = [6, 7, 8, 1, 2, 3, 4, 5]
target = 3

print(search_rotated(nums, target))  # Output: 5
print(search_rotated(nums, 6))  # Output: 0
print(search_rotated(nums, 9))  # Output: -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1

print(search_rotated([1], 0))  # Output: -1
print(search_rotated([1], 1))  # Output: 0
