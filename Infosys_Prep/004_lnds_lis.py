# Longest Increasing Subsequence (LIS) - Dynamic Programming Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Longest Increasing Subsequence (LIS) problem finds the length of the longest subsequence in a given sequence such that all elements of the subsequence are sorted in increasing order.

# Longest Non-Decreasing Subsequence: can be found by changing the condition from arr[j] < arr[i] to arr[j] <= arr[i]
def length(arr):
    n = len(arr)
    dp = [1] * n   # dp[i] = LIS ending at i

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:           # strictly increasing "<" | non-decreasing "<="
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Length of LIS is", length(arr))  # Output: 6


from collections import defaultdict

def lnds_with_xor(arr, M):
    n = len(arr)
    dp = [defaultdict(int) for _ in range(n)]

    for i in range(n):
        # start new subsequence
        dp[i][arr[i]] = 1

        for j in range(i):
            if arr[j] <= arr[i]:   # LNDS condition
                for old_xor, length in dp[j].items():
                    new_xor = old_xor ^ arr[i]
                    dp[i][new_xor] = max(dp[i][new_xor], length + 1)

    ans = 0
    for i in range(n):
        for xor_val, length in dp[i].items():
            if xor_val >= M:
                ans = max(ans, length)

    return ans
# Example usage:
arr = [6, 1, 2, 3, 2, 5]
M = 4
print("Length of LNDS with XOR >= M is", lnds_with_xor(arr, M))  # Output: 5