"""
#1416: 2진수 변환
"""

n = int(input())
ans = []

while n > 1:
    temp = n % 2
    n //= 2
    ans.append(temp)
ans.append(n)

ans.reverse()
print(*ans, sep="")
