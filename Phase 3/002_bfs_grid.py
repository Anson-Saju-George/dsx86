def bfs_grid(grid, sr, sc):
    n, m = len(grid), len(grid[0])
    q = deque([(sr, sc)])
    visited = {(sr, sc)}

    while q:
        r, c = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc))


dirs = [(1,0), (-1,0), (0,1), (0,-1)]

