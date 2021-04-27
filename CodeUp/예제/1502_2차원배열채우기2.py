"""
#1502: 2차원 배열 채우기 2
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(0, n):
        print(n * j + i, end=" ")
    print()
