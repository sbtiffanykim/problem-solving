n, k = map(int, input().split())
count = 0

# 나누기를 최대한 많이 할 때 가장 적게 연산할 수 있다
while True:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    count += 1
    if n == 1:
        break

print(count)