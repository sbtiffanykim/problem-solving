"""
#77484: 로또의 최고 순위와 최저 순위
"""


def result(point):
    if point == 6:
        return 1
    elif point == 5:
        return 2
    elif point == 4:
        return 3
    elif point == 3:
        return 4
    elif point == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []

    matching_num = 0
    zero_num = 0

    for l in lottos:
        if l in win_nums:
            matching_num += 1
        if l == 0:
            zero_num += 1

    max_point = matching_num + zero_num
    min_point = matching_num

    answer.append(result(max_point))
    answer.append(result(min_point))

    return answer