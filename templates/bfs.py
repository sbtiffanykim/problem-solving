from collections import deque

# 행/열 입력 받기
n, m = map(int, input().split())
# 그래프 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 방문기록 처리를 위한 list 초기화
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    # 큐 구현
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어나면 무시 (런타임 에러 방지하기 위해 가장 먼저 확인!)
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            # # 벽인 경우 무시
            # if graph[nx][ny] == 0: continue
            # 이미 방문한 노드일 경우에 무시
            if visited[nx][ny]:
                continue

            # 방문하지 않았다면 큐에 넣고 방문처리를 함
            queue.append((nx, ny))
            visited[nx, ny] = 1