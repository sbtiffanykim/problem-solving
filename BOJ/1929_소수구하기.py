import math

n, m = map(int, input().split())


def prime_nums(m):
    arr = [True for i in range(m + 1)]
    for i in range(2, int(math.sqrt(m)) + 1):
        if arr[i]:
            j = 2
            while i * j <= m:
                arr[i * j] = False
                j += 1
    return arr


arr = prime_nums(m)

for i in range(n, m + 1):
    # n이 1일 때 출력되지 않도록 고려해야 한다
    if arr[i] and i != 1:
        print(i)