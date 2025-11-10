class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        fresh_oranges, time = 0, 0
        queue = deque()  # (x, y, time)

        def bfs():
            nonlocal fresh_oranges, time
            while queue:
                x, y, t = queue.popleft()
                time = t
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # Skip if out of bounds, or not a fresh orange
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    queue.append((nx, ny , t + 1))

        for i in range(m):
            for j in range(n):
                # Count fresh oranges
                if grid[i][j] == 1:
                    fresh_oranges += 1
                # Add rotten oranges to the queue 
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        bfs()
        # If any fresh oranges left, return -1 
        return -1 if fresh_oranges else time
