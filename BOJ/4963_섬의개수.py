from collections import deque

# 이동할 수 있는 상, 하, 좌, 우 , 대각선(4) 방향 정의
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def bfs(x, y, dist):
    q = deque()
    # 시작점 큐에 넣기
    q.append((x, y))
    # 시작점 방문 처리
    dist[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 추가하면 무시
            if nx >= h or ny >= w or nx < 0 or ny < 0:
                continue
            # 방문한 적이 있는 위치거나 바다인 경우 무시
            if dist[nx][ny] > 0 or graph[nx][ny] == 0:
                continue
            # 해당 위치 큐에 넣기
            q.append((nx, ny))
            # 해당 위치에 방문처리
            dist[nx][ny] = 1


while True:
    w, h = map(int, input().split())

    # 0 0이 입력되면 종료
    if w == 0 and h == 0:
        break

    # 그래프 입력 받기
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    # 방문기록을 저장하는 리스트
    dist = [[0] * w for _ in range(h)]

    # 섬의 개수를 저장하는 변수
    cnt = 0
    for i in range(h):
        for j in range(w):
            # 땅이고 방문한 적이 없으면
            if graph[i][j] == 1 and dist[i][j] == 0:
                # BFS 후 섬의 개수를 증가시킴
                bfs(i, j, dist)
                cnt += 1

    print(cnt)