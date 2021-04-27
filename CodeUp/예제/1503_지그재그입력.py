"""
#1503: 지그재그 입력
"""

n = int(input())

for i in range(0, n):
    for j in range(1, n + 1):
        if (i + 1) % 2 != 0:
            print(n * i + j, end=" ")
        else:
            print(n * (i + 1) - (j - 1), end=" ")
    print()
