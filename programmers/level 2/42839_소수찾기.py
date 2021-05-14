from itertools import permutations
import math


def check_prime(n):

    # 판정할 숫자가 0 or 1이면 소수가 아니므로 False 반환 후 종료
    if n < 2:
        return False
    # 2부터 n sqared까지의 숫자로 n을 나누었을 때 나누어 떨어지면 소수가 아니다
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    # 위의 경우가 모두 아니면 소수이므로 True 반환 후 종료
    return True


def solution(numbers):
    answer = 0

    # 숫자 조합에 의해 만들어진 소수 저장
    prime_list = []
    for i in range(1, len(numbers) + 1):
        # 자릿수 별로 만들어 질 수 있는 수 구하기
        perlist = set(map("".join, list(permutations(numbers, i))))

        for k in perlist:
            # 그 수가 소수로 판정되면 prime_list에 넣기
            if check_prime(int(k)):
                prime_list.append((int(k)))

    # 11과 011을 같게 처리해줘야하므로 중복을 없애기 위해 set을 사용
    # 소수의 개수를 구해 정답을 낸다
    answer = len(set(prime_list))

    return answer