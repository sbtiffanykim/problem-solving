from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 범위 벗어나면 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            # 미로의 길이 아니면 무시
            if maze[nx][ny] == 0:
                continue
            # 미로에서의 길이고, 처음 지나가는 길일 때 시행
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                # 최단거리 증가
                maze[nx][ny] = maze[x][y] + 1

    # (n,m)까지의 최단거리 반환
    return maze[n - 1][m - 1]


# 출발지점에서 BFS 수행 결과 출력
print(bfs(0, 0))