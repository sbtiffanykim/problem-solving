from collections import deque

n, m, v = map(int, input().split())
# 작성 편의를 위해 index 0을 dummy index로 설정
graph = [[] for _ in range(n + 1)]

# 각 노드에 연결된 노드들을 추가한다
# 양방향이므로 서로 넣어줘야 함 (eg. graph[1][2] == graph[2][1])
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 작은 수의 노드부터 탐색하기를 원하므로 각 노드에 연결되어있는 노드들을 오름차순으로 정렬
for i in range(n + 1):
    graph[i].sort()

# 작성 편의를 위해 index 0을 dummy index로 설정
visited_d = [False] * (n + 1)
# 작성 편의를 위해 index 0을 dummy index로 설정
visited_b = [False] * (n + 1)
# DFS 결과를 담을 리스트
res_d = []
# BFS 결과를 담을 리스트
res_b = []


def dfs(v, graph):
    visited_d[v] = True
    res_d.append(v)
    # print(v, end=" ")
    for k in graph[v]:
        if not visited_d[k]:
            dfs(k, graph)
    return res_d


def bfs(v, graph):
    queue = deque()
    visited_b[v] = True
    queue.append(v)
    while queue:
        v = queue.popleft()
        res_b.append(v)
        # print(v, end=" ")
        for i in graph[v]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True
    return res_b


d = dfs(v, graph)
b = bfs(v, graph)
print(*d, sep=" ")
print(*b, sep=" ")
