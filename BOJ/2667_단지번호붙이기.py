from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))
visited = [[0] * n for _ in range(n)]
answer = []


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    # 넓이를 저장하기 위한 변수
    area = 0
    while queue:
        x, y = queue.popleft()
        # pop할 때마다 area를 증가시켜 총 면적 구하기
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 초과하면 무시
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            # 단지 안에 포함되어있지 않거나 이미 방문했다면 무시
            if board[nx][ny] != 1 or visited[nx][ny] != 0:
                continue
            # 해당 노드에 방문 표시
            visited[nx][ny] = 1
            # 큐에 삽입
            queue.append((nx, ny))
    # 한 단지를 모두 찾았다면 그 면적을 answer list에 넣기
    answer.append(area)


for i in range(n):
    for j in range(n):
        # 단지에 포함되어 있고 방문하지 않았다면
        if board[i][j] == 1 and visited[i][j] == 0:
            # 해당 노드에 대해 bfs 실행
            bfs(i, j)

# 각 단지 면적을 오름차순으로 정렬
answer.sort()
# 단지 수 출력
print(len(answer))
print(*answer, sep="\n")
