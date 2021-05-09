# Depth First Search(DFS)
# src: 이것이 취업을 위한 코딩테스트다 p.142


# 깊이를 우선으로 하여 모든 노드를 탐색한다


def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드 중 방문하지 않은 노드를 재귀적으로 방문한다
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 나타낸 2차원 리스트
graph = [
    [],  # 인덱스와 숫자를 맞추기 위한 빈 리스트
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드가 방문된 정보를 나타낸 2차원 리스트
visited = [False] * 9

dfs(graph, 1, visited)