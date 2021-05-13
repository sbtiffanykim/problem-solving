import math

n = int(input())
fac_n = str(math.factorial(n))

cnt = 0
for i in range(len(fac_n) - 1, -1, -1):
    if fac_n[i] != "0":
        break
    cnt += 1

print(cnt)