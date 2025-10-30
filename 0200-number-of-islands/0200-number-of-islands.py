class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # bfs
        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # Skip if out of bounds, already visited, or not land
                    if nx < 0 or nx >=m or ny < 0 or ny >= n or grid[nx][ny] != '1':
                        continue
                    grid[nx][ny] = '-1'  # Mark land as visited
                    queue.append((nx, ny))
        
        for i in range(m): 
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '-1'  # Mark land as visited
                    bfs(i, j)
                    ans += 1
        
        return ans