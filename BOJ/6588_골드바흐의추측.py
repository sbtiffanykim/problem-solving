import math
import sys

input = sys.stdin.readline


def prime_num(n):
    arr = [1] * (n + 1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if arr[i] == 1:
            j = 2
            while i * j <= n:
                arr[i * j] = 0
                j += 1
    return arr


prime_nums = prime_num(1000000)


while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n, 2):
        if prime_nums[i]:
            if prime_nums[n - i]:
                print(f"{n} = {i} + {n-i}")
                break