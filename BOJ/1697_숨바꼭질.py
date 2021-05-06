from collections import deque

n, k = map(int, input().split())
# 최대 움직일 수 있는 칸 만큼 범위 정하고 list 초기화
dist = [-1] * (100001)
queue = deque()

# 시작점 queue에 넣고 dist에 0을 넣어 시작점이라는 것을 나타낸다
queue.append(n)
dist[n] = 0

# 동생이 있는 지점에 도착하기 전까지 반복해서 시행
while dist[k] == -1:
    v = queue.popleft()
    # 1초 후에 움직일 수 있는 위치에서 조건 만족하는 지 확인
    for next in (v - 1, v + 1, 2 * v):
        # 범위 벗어나면 무시
        if next < 0 or next > 100000:
            continue
        # 이미 방문했을 경우 무시
        if dist[next] != -1:
            continue
        # 다음 이동 위치에 초를 더하고 queue에 삽입한다
        dist[next] = dist[v] + 1
        queue.append(next)

# 동생이 위치한 거리까지 걸리는 최소 시간 출력
print(dist[k])
