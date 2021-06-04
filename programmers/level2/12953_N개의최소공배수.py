import math


def solution(arr):
    answer = 0
    # gcd 찾기 위해 오름차순으로 정렬
    arr.sort()

    res = arr[0]
    # 두번째 원소부터 리스트의 끝까지 반복
    for i in range(1, len(arr)):
        # 바로 전에 구한 lcm과 현재 값의 gcd 구하기
        temp_gcd = math.gcd(res, arr[i])
        # lcm = a * b // gcd(a, b)
        res *= arr[i] // temp_gcd
    answer = res

    return answer


"""
print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))  # 6
"""