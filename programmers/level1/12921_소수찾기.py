import math


def prime_nums(n):
    # 0(index error방지), 1은 포함할 수 없음
    # 소수 판정을 위해 n+1개만큼 리스트 설정
    nums = [False, False] + [True] * (n - 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i] == True:
            # 배수들은 false로 설정
            for j in range(i + i, n + 1, i):
                nums[j] = False
    return nums.count(True)


def solution(n):
    answer = 0
    answer = prime_nums(n)
    return answer


"""
정답확인용 테스트 케이스
print((solution(10)))  #4
print((solution(5)))   #3
"""