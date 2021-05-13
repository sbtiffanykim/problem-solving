import math
import sys
import time

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


def goldbach_conjecture(arr):
    for i in range(3, len(arr) + 1, 2):
        if arr[i]:
            t = n - i
            if arr[t]:
                print(f"{n} = {i} + {t}")
                return
    print('"Goldbach\'s conjecture is wrong."')


while True:
    start_time = time.time()
    n = int(input())
    if n == 0:
        break
    arr = prime_num(n)
    goldbach_conjecture(arr)
    end_time = time.time()
    print(end_time - start_time)