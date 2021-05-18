import sys

input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))

houses.sort()
# 집의 개수가 홀수고, median값과 그 앞의 값이 같지 않을 때
if n % 2 != 0 and houses[n // 2] != houses[n // 2 - 1]:
    idx = n // 2
# 이외의 경우
else:
    idx = n // 2 - 1

print(houses[idx])