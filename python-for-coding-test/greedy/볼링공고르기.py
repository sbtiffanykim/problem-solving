from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

res = list((combinations(balls, 2)))
count = len(res)

# 무게가 같으면 빼기
for i in res:
    if i[0] == i[1]:
        count -= 1

print(count)