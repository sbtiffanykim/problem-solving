n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))
vis = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    stack = []
    stack.append((x, y))
    vis[x][y] = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if vis[nx][ny] != -1:
                continue
            vis[nx][ny] = 1
            stack.append((nx, ny))


for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            vis[i][j] = -1
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and vis[i][j] == -1:
            dfs(i, j)
            cnt += 1

print(cnt)