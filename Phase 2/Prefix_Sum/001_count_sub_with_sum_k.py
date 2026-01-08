# Count subarrays with sum equal to k

from collections import defaultdict


from collections import defaultdict

def count_subarrays_with_sum(nums, k):
    prefix = 0
    answer = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1   # prefix sum before starting (empty prefix)

    for value in nums:
        # prefix[j]
        prefix += value

        # prefix[i] = prefix[j] - k
        # derived from prefixSum[ j ] - prefixSum[ i-1 ] = k
        required_prefix = prefix - k
#       prefixSum[i-1] ----> prefixSum[j]
#           req_prefix         prefix

        # count how many such prefix[i] exist
        answer += prefix_count[required_prefix] # check if required_prefix exists if so add its count

        # record prefix[j]
        prefix_count[prefix] += 1

    return answer



# Example usage:
nums = [1, 2, 3, 7, 5]
k = 12
print(count_subarrays_with_sum(nums, k))  # expect 2
nums = [1, 2, 3, 7, 5, -5, -7, 3]
print(count_subarrays_with_sum(nums, k))  # expect 3
