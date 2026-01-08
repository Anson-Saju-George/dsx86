def count_good_nodes(n, par, val, K):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[par[i]].append(i)

    count = 0

    def dfs(u):
        nonlocal count
        s = val[u]
        for v in tree[u]:
            s += dfs(v)
        if s >= K:
            count += 1
        return s

    dfs(1)
    return count

# Example usage:
n = 5
par = [0, 0, 1, 1, 2, 2]  # 1-based indexing; par[1] = 0 (root)
val = [0, 1, 2, 3, 4, 5]  # 1-based indexing; val[1] = 1
K = 10
print(count_good_nodes(n, par, val, K))  # Output: 3