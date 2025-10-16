class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        m, n = len(image), len(image[0])       
        visited = [[False for _ in range(n)] for _ in range(m)]
        starting_color = image[sr][sc]

        queue = deque()
        queue.append((sr, sc))
        visited[sr][sc] = True
        image[sr][sc] = color

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # skip cells that are out of bounds, visited, or not the starting color
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny] or image[nx][ny] != starting_color:
                    continue
                visited[nx][ny] = True
                image[nx][ny] = color
                queue.append((nx, ny))
        
        return image
