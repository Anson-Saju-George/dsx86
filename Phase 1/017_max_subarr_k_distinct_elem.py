def max_subarray_sum_k_distinct(arr, k):
    l = 0
    curr_sum = 0
    freq = {}
    best = 0
    n = len(arr)

    for r in range(n):
        # add arr[r]
        curr_sum += arr[r]
        freq[arr[r]] = freq.get(arr[r], 0) + 1

        # shrink window if distinct count > k
        while len(freq) > k:
            # remove arr[l]
            freq[arr[l]] -= 1
            curr_sum -= arr[l]

            if freq[arr[l]] == 0:
                del freq[arr[l]]

            l += 1

        # update best
        best = max(best, curr_sum)

    return best

# Example usage:
arr = [1, 2, 1, 2, 3, 4, 5]
k = 3
print(max_subarray_sum_k_distinct(arr, k))  # expect 12 (subarray [3,4,5])