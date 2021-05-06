from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
# 불 이동 기록하기 위한 list
f_dist = [[-1] * m for _ in range(n)]
# 지훈이 이동 기록하기 위한 list
j_dist = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

f_queue = deque()
j_queue = deque()


def bfs():
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        if nx >= n or ny >= m or nx < 0 or ny < 0:
            continue
        if board[nx][ny] == "#" or f_dist[nx][ny] >= 0:
            continue
        f_dist[nx][ny] = f_dist[x][y] + 1
        f_queue.append((nx, ny))

    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        # 지훈이는 가장자리 접한 공간에서는 탈출할 수 있으므로 시간 출력(+1) 후 종료
        if nx >= n or ny >= m or nx < 0 or ny < 0:
            return j_dist[nx][ny] + 1
        # 벽이거나 이동 불가 지역에서는 무시
        if board[nx][ny] == "#" or j_dist[nx][ny] >= 0:
            continue
        # 불 이동시간 <= 지훈이 이동시간이면 이동 불가
        # the most important part in the code
        if f_dist[nx][ny] != -1 and f_dist[nx][ny] <= j_dist[x][y] + 1:
            continue
        j_dist[nx][ny] = j_dist[x][y] + 1
        j_queue.append((nx, ny))

    return "IMPOSSIBLE"


for i in range(n):
    for j in range(m):
        if board[i][j] == "J":
            j_dist[i][j] = 0
            j_queue.append((i, j))
        elif board[i][j] == "F":
            f_dist[i][j] = 0
            f_queue.append((i, j))

print(bfs())