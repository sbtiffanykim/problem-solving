"""
#1403: 배열 두번 출력하기 1
"""

n = int(input())
nums = list(map(int, input().split()))

for _ in range(2):
    print(*nums, sep="\n")
