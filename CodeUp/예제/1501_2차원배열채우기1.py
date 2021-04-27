"""
#1501: 2차원 배열 채우기 1
"""

n = int(input())

for i in range(1, n * n + 1):
    print(i, end=" ")
    if i % n == 0:
        print()
