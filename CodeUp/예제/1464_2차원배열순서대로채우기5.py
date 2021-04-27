"""
#1464: 2차원 배열 순서대로 채우기 1-5
"""

n, m = map(int, input().split())

k = n * m

for i in range(n):
    for j in range(m):
        print(k, end=" ")
        k -= 1
    print()
