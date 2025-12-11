# Given a sorted array `arr` and a value `target`,
# find the FIRST index `i` such that:

#     arr[i] >= target

# If such an index does not exist, return len(arr).
# This is also known as the "lower bound".

# Similarly, find the LAST index `j` such that:
#     arr[j] <= target


def first_ge(arr, target):
    left, right = 0, len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans # or len(arr)


# Given a sorted array `arr` and a value `target`,
# find the LAST index `i` such that:

#     arr[i] <= target

# If such an index does not exist, return -1.
# This is also known as the "upper bound - 1" or -1.


def last_le(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans or -1


# Example usage:
arr = [1, 2, 4, 4, 4, 7, 9]

first_ge(arr, 4)  # → 2
first_ge(arr, 5)  # → 5
first_ge(arr, 10)  # → 7

last_le(arr, 4)  # → 4
last_le(arr, 3)  # → 1
last_le(arr, 0)  # → -1
