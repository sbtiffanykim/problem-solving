"""
#1420: 3등 찾기
"""

n = int(input())
arr = []

for i in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

arr = sorted(arr, key=lambda x: x[1], reverse=True)
print(arr[2][0])