"""
#6089: 수 나열하기 2
"""

a, r, n = map(int, input().split())

for i in range(1, n):
    a *= r

print(a)
