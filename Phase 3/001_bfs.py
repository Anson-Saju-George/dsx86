from collections import deque

def bfs(adj, start):
    q = deque([start])
    visited = {start}
    dist = {start: 0}

    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                dist[v] = dist[u] + 1
                q.append(v)

    return dist

