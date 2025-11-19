class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')  # Put max value to calculate minimum distance
                else:
                    queue.append((i, j))
        print(queue)
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # Ignore if out of bounds or not 1
                if nx < 0 or nx >= m or ny < 0 or ny >= n or mat[nx][ny] != float('inf'):
                    continue
                mat[nx][ny] = 1 + mat[x][y]
                queue.append((nx, ny))

        return mat