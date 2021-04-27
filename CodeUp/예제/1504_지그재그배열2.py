"""
#1504: 지그재그 배열 2
"""

n = int(input())
arr = [[0] * n for i in range(n)]

k = 1
for i in range(0, n):
    for j in range(0, n):
        if i % 2 == 0:
            arr[j][i] = k
        else:
            arr[n - j - 1][i] = k
        k += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
