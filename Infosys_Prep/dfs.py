from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def sum_of_all_subtree_sums(n, par, a):
    # Build adjacency list
    tree = defaultdict(list)
    for child in range(2, n + 1):
        parent = par[child]
        tree[parent].append(child)

    ans = 0

    def dfs(u):
        nonlocal ans
        curr_sum = a[u]          # include node itself
        for v in tree[u]:
            curr_sum += dfs(v)   # add subtree sums of children
        ans += curr_sum          # add subtree_sum(u) to answer
        return curr_sum

    dfs(1)   # root is 1
    return ans


n = 5
par = {
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 2
}
a = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5
}

print(sum_of_all_subtree_sums(n, par, a))  # Output: 38
