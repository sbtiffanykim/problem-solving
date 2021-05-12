from collections import deque

n = int(input())
e = int(input())
graph = [[] for _ in range(n + 1)]
vis = [0] * (n + 1)


def bfs(v):
    q = deque()
    q.append(v)
    vis[v] = 1
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        for i in graph[x]:
            if vis[i] == 0:
                q.append(i)
                vis[i] = 1
    return cnt


# 그래프 입력받기
for _ in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# q에서 pop할 때 1번 컴퓨터도 빠지므로 자기 자신(1번 컴퓨터)을 제외하기 위해 1을 뺌
print(bfs(1) - 1)
