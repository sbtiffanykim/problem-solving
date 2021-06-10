from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    # 첫번째 원소를 더하고 뺀 값을 queue에 넣기
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))

    # bfs 실행
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        # numbers의 끝까지
        if idx < len(numbers):
            # 다음 인덱스 값을 더하고 빼서 queue에 넣기
            for i in [-1, 1]:
                queue.append((temp + i * numbers[idx], idx))
        # numbers 내의 모든 값을 더하고 뺐을 때
        else:
            # target값과 같으면 정답 개수 증가
            if temp == target:
                answer += 1

    return answer


"""
print(solution([1, 1, 1, 1, 1]), 3)   # 5
"""