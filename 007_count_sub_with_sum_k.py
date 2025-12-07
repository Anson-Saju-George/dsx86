from collections import defaultdict


def count_subarrays_with_sum(nums, k):
    prefix_sum = 0
    count = 0

    # freq[sum] = how many times this prefix sum has appeared
    freq = defaultdict(int)
    freq[0] = 1  # important: empty prefix

    for x in nums:
        prefix_sum += x

        # We want: prefix_sum - prev_prefix = k
        # => prev_prefix = prefix_sum - k
        need = prefix_sum - k

        # all previous prefixes with value `need` form valid subarrays ending here
        count += freq[need]

        # record this prefix_sum for future subarrays
        freq[prefix_sum] += 1

    return count


if __name__ == "__main__":
    nums = [1, 2, 3, -2, 5]
    k = 3
    print(count_subarrays_with_sum(nums, k))  # expect 3
