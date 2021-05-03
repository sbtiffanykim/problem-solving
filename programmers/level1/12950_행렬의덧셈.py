"""
#12950: 행렬의 덧셈
"""


def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        answer.append(list(map(lambda x, y: x + y, i, j)))

    return answer


# 입출력 확인
print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
