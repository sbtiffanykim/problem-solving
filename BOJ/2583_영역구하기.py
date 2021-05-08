from collections import deque

m, n, k = map(int, input().split())
# 모눈종이를 모두 0으로 초기화
board = [[0] * m for _ in range(n)]
# 주어진 좌표를 따른 직사각형을 모눈종이에 -1로 채운다
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            # -1인 곳은 영역으로 간주될 수 없다
            board[i][j] = -1

# 이동 가능 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 이미 방문했다는 표시를 남기기 위해 1로 값을 변경
    board[x][y] = 1
    # 영역의 넓이를 저장하기 위한 변수
    cnt = 0
    while queue:
        x, y = queue.popleft()
        # pop할때마다 넓이를 하나씩 늘림
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 초과할 경우 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            # 모눈 종이가 채워져있거나, 이미 방문된 영역일 경우 무시
            if board[nx][ny] != 0:
                continue
            # 해당 영역을 방문했다는 표시를 남긴다
            board[nx][ny] = 1
            queue.append((nx, ny))
    return cnt


# 영역들을 저장하기 위한 list
res = []
for i in range(n):
    for j in range(m):
        # 방문하지 않고, 직사각형이 차지하지 않는 영역일 경우 BFS 실행
        # 해당 영역의 넓이를 res list에 넣는다
        if board[i][j] == 0:
            res.append(bfs(i, j))

# 영역의 크기를 오름차순으로 정렬
res.sort()
# 영역 개수 출력
print(len(res))
# 넓이 출력
print(*res, sep=" ")
