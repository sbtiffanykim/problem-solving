from itertools import combinations
from math import gcd

t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    a = a[1:]
    a = combinations(a, 2)
    res = 0
    for i in a:
        res += gcd(i[0], i[1])
    print(res)
