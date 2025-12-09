def kandane(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    start = end = 0
    sub_start = 0

    for i in range(1, len(nums)):
        x = nums[i]

        if curr_sum + x < x:
            curr_sum = x
            sub_start = i
        else:
            curr_sum += x

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = sub_start
            end = i

    return max_sum, nums[start : end + 1], start, end


# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray, start, end = kandane(nums)
print("Input Array       :", nums)
print("Max Subarray Sum  :", max_sum)
print("Subarray          :", subarray)
print("Start Index       :", start)
print("End Index         :", end)
