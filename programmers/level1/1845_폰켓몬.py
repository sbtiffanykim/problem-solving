"""
#1845: 폰켓몬
"""


def solution(nums):
    answer = 0

    n = len(nums)
    # 중복 제거해서 현재 폰켓몬 종류를 저장
    nums_w = set(nums)

    # 현재 종류수가 가져갈 수 있는 인형 개수보다 더 많으면 N/2만큼만 가져가면 됨
    if len(nums_w) >= n / 2:
        answer = n / 2
    # 현재 종류수가 가져가야할 인형 개수보다 작다면 현재의 종류수가 가장 많은 종류의 폰켓몬을 선택하는 방법이 됨
    else:
        answer = len(nums_w)

    return answer