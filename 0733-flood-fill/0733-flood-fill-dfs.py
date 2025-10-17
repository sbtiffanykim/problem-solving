class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        m, n = len(image), len(image[0])       
        starting_color = image[sr][sc]
        if starting_color == color:
            return image  # no need to fill

        def dfs(x, y):
            # skip out-of-bounds or different color cells
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != starting_color:
                return
            if image[x][y] == starting_color:
                image[x][y] = color
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
            
        dfs(sr, sc)
        return image