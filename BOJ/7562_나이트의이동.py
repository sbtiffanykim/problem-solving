from collections import deque

T = int(input())

# 나이트 이동 가능 방향 정의
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]


def bfs(x, y, des_x, des_y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 무시
            if nx >= l or ny >= l or nx < 0 or ny < 0:
                continue
            # 이미 이동했던 위치라면 무시
            if dist[nx][ny] > 0:
                continue
            # 이동할 위치와 목적지가 같다면 시도횟수 반환 후 BFS 종료
            if nx == des_x and ny == des_y:
                return dist[x][y] + 1
            # 위의 경우가 아니라면 이동 후 위치를 queue에 넣기
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))


for _ in range(T):
    l = int(input())
    # 나이트 위치 기록하기 위한 list 초기화
    dist = [[0] * l for _ in range(l)]
    # 현재 위치
    cur_x, cur_y = map(int, input().split())
    # 목적지
    des_x, des_y = map(int, input().split())
    # 목적지와 출발지가 같다면 BFS 돌릴 필요 없으므로 0 출력
    if cur_x == des_x and cur_y == des_y:
        print(0)
    # BFS 수행 결과 출력
    else:
        print(bfs(cur_x, cur_y, des_x, des_y))
