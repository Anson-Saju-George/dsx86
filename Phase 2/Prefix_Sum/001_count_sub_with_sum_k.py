# Count subarrays with sum equal to k

from collections import defaultdict


def count_subarrays_with_sum(nums, k):
    prefix_sum = 0
    count = 0
    freq = defaultdict(
        int
    )  # prefix sum frequency i.e how many times a prefix sum has occurred
    freq[0] = 1  # important: empty prefix

    for x in nums:
        prefix_sum += x  # current prefix sum
        need = prefix_sum - k  # we need this prefix sum to form a subarray with sum k
        count += freq[need]  # add the number of times 'need' has occurred
        freq[prefix_sum] += 1  # update the frequency of the current prefix sum

    return count


# Example usage:
nums = [1, 2, 3, 7, 5]
k = 12
print(count_subarrays_with_sum(nums, k))  # expect 3
