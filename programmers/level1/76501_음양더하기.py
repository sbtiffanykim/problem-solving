"""
#76501: 음양 더하기
"""


def solution(absolutes, signs):
    answer = 0

    for i in zip(absolutes, signs):
        if not ((i)[1]):
            answer += i[0] * -1
        else:
            answer += i[0]

    return answer