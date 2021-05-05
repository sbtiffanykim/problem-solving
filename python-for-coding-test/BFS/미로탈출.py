from collections import deque

# 행, 열 입력받기
n, m = map(int, input().split())
# 그래프 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
# 이동방향 초기화(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]


def dfs(x, y):
    # queue 구현 위해 deque 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            dy = y + dy[i]
            # 범위를 넘어설 경우 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            # 벽일 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 미로이고, 처음 갔을 때만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래 최단거리 반환
    return graph[n - 1][m - 1]


print(bfs(0, 0))