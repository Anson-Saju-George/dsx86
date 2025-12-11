from collections import defaultdict
from typing import List, Tuple, Optional

def count_subarrays_with_sum(nums: List[int], k: int) -> int:
    """
    Count number of contiguous subarrays with sum == k.
    O(n) time, O(n) space.
    """
    prefix_sum = 0
    freq = defaultdict(int)
    freq[0] = 1  # empty prefix

    count = 0
    for x in nums:
        prefix_sum += x
        need = prefix_sum - k
        count += freq[need]
        freq[prefix_sum] += 1

    return count


def longest_subarray_with_sum(nums: List[int], k: int) -> Tuple[int, Optional[int], Optional[int]]:
    """
    Return tuple (length, start_index, end_index) of the longest contiguous subarray with sum == k.
    If none found, returns (0, None, None).
    Uses prefix-sum -> earliest-index map to achieve O(n).
    """
    prefix_sum = 0
    # store earliest occurrence of a prefix sum
    first_occurrence = {0: -1}  # prefix 0 at index -1 (helps subarrays starting at 0)
    
    best_len = 0
    best_start = None
    best_end = None

    for i, x in enumerate(nums):
        prefix_sum += x
        # if we've seen prefix_sum - k before, there's a subarray (prev_index+1 ... i) summing to k
        need = prefix_sum - k
        if need in first_occurrence:
            start_idx = first_occurrence[need] + 1
            length = i - first_occurrence[need]
            if length > best_len:
                best_len = length
                best_start = start_idx
                best_end = i

        # only record earliest occurrence to maximize later lengths
        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = i

    if best_len == 0:
        return 0, None, None
    return best_len, best_start, best_end


# Example usage:

nums = [1, 2, 3, 7, 5]

k = 12

cnt = count_subarrays_with_sum(nums, k)
length, s, e = longest_subarray_with_sum(nums, k)
print("count:", cnt)                  # expected: 2
print("longest length:", length)      # expected: 3
print("longest indices:", (s, e))     # expected: (1, 3)

# longest subarray values:
if s is not None:
    print("longest subarray:", nums[s:e+1])  # expected: [2, 3, 7]
