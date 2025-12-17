def dfs_grid(grid, r, c, visited):
    n, m = len(grid), len(grid[0])
    stack = [(r, c)]
    visited.add((r, c))

    while stack:
        x, y = stack.pop()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == '1' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
