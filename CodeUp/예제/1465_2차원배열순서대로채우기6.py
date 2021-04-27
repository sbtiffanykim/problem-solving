"""
#1465: 2차원 배열 순서대로 채우기 1-6
"""

n, m = map(int, input().split())


for i in range(n, 0, -1):
    k = i * m - m + 1
    for j in range(m):
        print(k + j, end=" ")
    print()
