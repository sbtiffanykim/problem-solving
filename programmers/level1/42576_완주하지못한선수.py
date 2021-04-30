"""
#42576: 완주하지 못한 선수
"""


from collections import Counter


def solution(participant, completion):
    answer = ""

    # 리스트 내에서 각각의 이름과 그 수를 나타내는 dict를 Counter를 이용하여 만듦
    # 둘을 빼면 동명이인 변수를 제외하고 완주하지 못한 사람이 구해짐
    answer = list((Counter(participant) - Counter(completion)))[0]

    return answer