"""
Kandane's Algorithm to find the maximum sum of a contiguous subarray.
Kandane's algorithm aka Maximum Subarray Problem.

Steps:
1. Initialize two variables: max_current and max_global to the first element of the array.
2. Iterate through the array starting from the second element.
3. For each element, update max_current to be the maximum of the current element and max_current plus the current element.
4. Update max_global to be the maximum of max_global and max_current.
5. Return max_global as the result.

This implementation also returns the subarray itself.
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Think of it as a bus that can either start a new route
# at the current stop or continue on its existing route
# by adding the current stop's passengers.


def kadane(nums):
    max_sum = nums[0]
    curr = nums[0]

    for x in nums[1:]:

        curr = max(x, curr + x)
        max_sum = max(max_sum, curr)

    return max_sum


def kadane_with_indices(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        x = nums[i]

        # either extend or restart window
        if curr_sum + x < x:
            curr_sum = x
            temp_start = i
        else:
            curr_sum += x

        # update best
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    return max_sum, start, end


# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(nums))
# Using the version that also returns indices
max_sum, start, end = kadane_with_indices(nums)
print("Max Subarray Sum:", max_sum)
print("Subarray:", nums[start : end + 1])
print("Indices:", (start, end))


print(kadane([5, -3, 5]))  # Output: 7