from itertools import combinations
import math


def prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    num = list(combinations(nums, 3))

    for n in num:
        if prime_num(sum(n)):
            answer += 1

    return answer

    """ 
    정답 확인용 테스트케이스
    print((solution[1, 2, 3, 4]))   #1
    print((solution[1, 2, 7, 6, 4])) #4
    """