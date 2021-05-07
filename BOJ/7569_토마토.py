from collections import deque

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
riped = [[[0] * m for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nz >= h or nx >= n or ny >= m or nx < 0 or ny < 0 or nz < 0:
                continue
            # -1이여야만 영향을 받으므로, 0이상일 경우 무시
            if riped[nz][nx][ny] >= 0:
                continue
            riped[nz][nx][ny] = riped[z][x][y] + 1
            queue.append((nz, nx, ny))


for i in range(h):
    for j in range(n):
        for k in range(m):
            # 익은 토마토는 시작점이므로 queue에 넣기
            if board[i][j][k] == 1:
                queue.append((i, j, k))
            # 익지 않은 토마토는 -1로 표시
            elif board[i][j][k] == 0:
                riped[i][j][k] = -1

bfs()

res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 익지 않은 토마토가 있다면 -1 출력
            if riped[i][j][k] == -1:
                res = -1
            elif res != -1:
                res = max(res, riped[i][j][k])

print(res)
