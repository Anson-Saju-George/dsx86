def has_cycle_directed(adj):
    visited = set()
    rec = set()

    def dfs(u):
        visited.add(u)
        rec.add(u)

        for v in adj[u]:
            if v not in visited:
                if dfs(v):
                    return True
            elif v in rec:
                return True

        rec.remove(u)
        return False

    for node in adj:
        if node not in visited:
            if dfs(node):
                return True
    return False
