import math


def divisor_num(n):
    # n==1이면 약수가 1개이므로 1을 return 후 종료
    if n == 1:
        return 1

    # 아니라면 1과 자기 자신을 먼저 약수 개수로 추가
    res = 2
    for i in range(2, int(math.sqrt(n) + 1)):
        # 약수 일 때
        if n % i == 0:
            # 제곱수인 경우 약수 1개만 추가
            if (n // i) == i:
                res += 1
            # 나머지는 2개 추가
            else:
                res += 2
    return res


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        # 약수의 개수가 짝수일 때는 더하기
        if divisor_num(i) % 2 == 0:
            answer += i
        # 약수의 개수가 홀수일 때는 빼기
        else:
            answer -= i

    return answer


"""
정답 확인용 테스트케이스
print((solution(13, 17)))  #43
print((solution(24, 27)))  #52
print((solution(1, 1)))    #-1
"""