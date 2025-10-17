class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        m, n = len(image), len(image[0])       
        starting_color = image[sr][sc]
        if starting_color == color:
            return image  # no need to fill

        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # skip cells that are out of bounds, visited, or not the starting color
                if nx < 0 or nx >= m or ny < 0 or ny >= n or image[nx][ny] != starting_color:
                    continue
                image[nx][ny] = color
                queue.append((nx, ny))
        
        return image