from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 그림 개수 저장하기 위한 변수
count = 0
# 가장 넓은 그림의 넓이 저장하기 위한 변수
mx = 0


def bfs(i, j):
    # queue 구현
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    # 그림 면적 구하기 위한 변수 설정
    area = 0
    # queue가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # popleft할 때마다 그림 면적을 하나씩 늘려간다
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나면 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            # 그림이 아니거나 이미 방문했다면 무시
            if graph[nx][ny] == 0 or visited[nx][ny]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    return area


for i in range(n):
    for j in range(m):
        # 그림 부분이 아니거나 이미 방문(하나의 그림으로 연결된)한 지점은 새로운 그림의 시작점이 될 수 없다
        if graph[i][j] == 0 or visited[i][j]:
            continue
        # 새로운 그림의 시작이므로 그림의 개수를 한 개 증가시킨다
        count += 1
        cur_area = bfs(i, j)
        mx = max(mx, cur_area)


print(count)
print(mx)