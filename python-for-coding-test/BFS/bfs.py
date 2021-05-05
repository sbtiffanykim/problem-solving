from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    # queue 구현을 위해 deque 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        # 해당 원소와 연결되었고, 아직 방문하지 않은 원소를 큐에 삽입한 후 방문처리 함
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited[i] = True


# 각 노드의 연결 정보를 나타냄
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 방문 정보를 위한 list 초기화
visited = [False] * 9

# bfs 호출
bfs(graph, 1, visited)