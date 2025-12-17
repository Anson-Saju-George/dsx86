def has_cycle_undirected(adj):
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for node in adj:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False
