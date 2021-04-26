"""
#1411: 빠진 카드
"""

n = int(input())
ans = [0] * n

for i in range(n - 1):
    card = int(input())
    ans[card - 1] += 1

print(ans.index(0) + 1)
