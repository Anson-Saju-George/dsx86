def subtree_sum(n, par, val):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[par[i]].append(i)

    res = [0]*(n+1)

    def dfs(u):
        s = val[u]
        for v in tree[u]:
            s += dfs(v)
        res[u] = s
        return s

    dfs(1)
    return res[1:]


# Example usage:
n = 5
par = [0, 0, 1, 1, 2, 2]  # 1-based indexing; par[1] = 0 (root)
val = [0, 1, 2, 3, 4, 5]  # 1-based indexing; val[1] = 1
print(subtree_sum(n, par, val))  # Output: [15, 11, 3, 4, 5]
# Explanation:
# Node 1: sum = 1 + 2 + 3 + 4 + 5 = 15
# Node 2: sum = 2 + 4 + 5 = 11
# Node 3: sum = 3
# Node 4: sum = 4
# Node 5: sum = 5

def subtree_max(n, par, val):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[par[i]].append(i)

    res = [0]*(n+1)

    def dfs(u):
        m = val[u]
        for v in tree[u]:
            m = max(m, dfs(v))
        res[u] = m
        return m

    dfs(1)
    return res[1:]

# Example usage:
n = 5
par = [0, 0, 1, 1, 2, 2]  # 1-based indexing; par[1] = 0 (root)
val = [0, 1, 5, 3, 4, 2]  # 1-based indexing; val[1] = 1
print(subtree_max(n, par, val))  # Output: [5, 5, 3, 4, 2]
# Explanation:
# Node 1: max = max(1, 5, 3, 4, 2) = 5
# Node 2: max = max(2, 4, 2) = 5
# Node 3: max = 3
# Node 4: max = 4
# Node 5: max = 2

def subtree_min(n, par, val):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[par[i]].append(i)

    res = [0]*(n+1)

    def dfs(u):
        m = val[u]
        for v in tree[u]:
            m = min(m, dfs(v))
        res[u] = m
        return m

    dfs(1)
    return res[1:]

# Example usage:
n = 5
par = [0, 0, 1, 1, 2, 2]  # 1-based indexing; par[1] = 0 (root)
val = [0, 5, 1, 3, 4, 2]  # 1-based indexing; val[1] = 5
print(subtree_min(n, par, val))  # Output: [1, 1, 3, 4, 2]
# Explanation:
# Node 1: min = min(5, 1, 3, 4, 2) = 1
# Node 2: min = min(1, 4, 2) = 1
# Node 3: min = 3
# Node 4: min = 4
# Node 5: min = 2

