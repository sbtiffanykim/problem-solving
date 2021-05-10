import math

n, m = map(int, input().split())
gcd = math.gcd(n, m)
lcm = int(n * m / gcd)
print(gcd, lcm, sep="\n")