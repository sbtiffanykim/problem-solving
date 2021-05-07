from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    queue = deque()

    # 배추 위치 입력받은 후 표시
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
        # 배추 위치를 나타내기 위해 -1로 초기화
        dist[y][x] = -1

    def bfs(x, y):
        queue.append((x, y))
        # 인접 면적 땅임을 표시
        dist[x][y] = 1
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위 초과 무시
                if nx >= n or ny >= m or nx < 0 or ny < 0:
                    continue
                # 이미 인접 면적으로 카운트 되었거나(>0) 배추가 없는 땅(=0이라면) 무시
                if dist[nx][ny] >= 0:
                    continue
                # 인접 면적 땅임을 표시
                dist[nx][ny] = 1
                queue.append((nx, ny))

    # 배추밭 개수 저장할 변수
    cnt = 0
    for i in range(n):
        for j in range(m):
            # 배추가 심어져있고, 아직 카운트 하지 않았다면 bfs하고, 배추밭 개수 더하기
            if board[i][j] == 1 and dist[i][j] == -1:
                cnt += 1
                bfs(i, j)

    print(cnt)