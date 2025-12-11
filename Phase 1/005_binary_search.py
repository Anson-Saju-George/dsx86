# Binary Search Implementation in Python


def binary_search(nums, target):
    left = 0  # Initialize left pointer
    right = len(nums) - 1  # Initialize right pointer

    while (
        left <= right
    ):  # Continue searching while the left pointer is less than or equal to the right pointer
        mid = (
            left + right
        ) // 2  # Calculate the middle index by taking the floor of the average of left and right

        if nums[mid] == target:  # Check if the middle element is the target
            return mid  # Target found, return the index

        elif nums[mid] < target:  # If target is greater, ignore left half
            left = mid + 1  # Move left pointer to mid + 1

        else:  # nums[mid] > target
            right = mid - 1  # If target is smaller, ignore right half

    return -1  # Target not found, return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(nums, 2))  # Output: 1
# print(binary_search(nums, 11)) # Output: -1
