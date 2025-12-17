def dfs(adj, u, visited):
    visited.add(u)
    for v in adj[u]:
        if v not in visited:
            dfs(adj, v, visited)

def dfs_iter(adj, start):
    stack = [start]
    visited = set()
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                stack.append(v)
    return visited
