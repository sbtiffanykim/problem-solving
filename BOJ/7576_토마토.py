# 시작점이 여러개인 BFS
from collections import deque

m, n = map(int, input().split())
# 토마토의 배열 입력받기
board = [list(map(int, input().split())) for _ in range(n)]
# 첫번째 익은 토마토로부터 걸리는 시간을 저장하기 위한 list 초기화
dist = [[0] * m for _ in range(n)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        # 가장 처음 익은 토마토의 위치(시작지점) 확인 후 queue에 넣기
        if board[i][j] == 1:
            queue.append((i, j))
        # 익지 않은 토마토의 위치(이동 가능 지점) 확인 후 구분을 위해 dist에 -1 넣기
        if board[i][j] == 0:
            dist[i][j] = -1

# BFS 실행
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    # 범위를 벗어나는 경우 무시
    if nx >= n or ny >= m or nx < 0 or ny < 0:
        continue
    # 이동 가능 지점이 아닐 경우 무시
    if dist[nx][ny] >= 0:
        continue
    dist[nx][ny] = dist[x][y] + 1
    queue.append((nx, ny))

res = 0
for i in range(n):
    for j in range(m):
        # 익지 않은 토마토가 남아있는 지 확인
        if dist[i][j] == -1:
            res = -1
        # 익지 않은 토마토가 없을 경우 최소 날짜 저장
        elif res != -1 and dist[i][j] > -1:
            res = max(res, dist[i][j])

print(res)