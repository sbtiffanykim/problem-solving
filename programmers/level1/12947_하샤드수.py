"""
#12947: 하샤드 수
"""


def solution(x):
    answer = True
    # 주어진 x의 각 자리수를 더하기 위해 str로 만들기
    n = map(int, str(x))
    s = sum(n)
    if x % s != 0:
        answer = False

    return answer


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))