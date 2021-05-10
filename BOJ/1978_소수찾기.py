import math

n = int(input())
nums = list(map(int, input().split()))


def is_prime_number(i):
    if i == 1:
        return False
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            return False
    return True


ans = 0
for k in nums:
    if is_prime_number(k):
        ans += 1

print(ans)