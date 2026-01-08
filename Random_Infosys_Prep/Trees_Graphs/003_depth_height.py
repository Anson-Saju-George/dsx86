def compute_depth(n, par):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[par[i]].append(i)

    depth = [0] * (n+1)

    def dfs(u, d):
        depth[u] = d
        for v in tree[u]:
            dfs(v, d + 1)

    dfs(1, 0)
    return depth[1:]

def compute_height(n, par):
    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        tree[par[i]].append(i)

    height = [0] * (n+1)

    def dfs(u):
        if not tree[u]:   # leaf
            height[u] = 0
            return 0

        max_child_height = 0
        for v in tree[u]:
            max_child_height = max(max_child_height, dfs(v))

        height[u] = max_child_height + 1
        return height[u]

    dfs(1)
    return height[1:]

# Example usage:
n = 5
par = [0, 0, 1, 1, 2, 2]  # 1-based indexing; par[1] = 0 (root)
print("Depths:", compute_depth(n, par))  # Output: [0, 1, 1, 2, 2]
print("Heights:", compute_height(n, par))  # Output: [2, 1, 0, 0, 0]