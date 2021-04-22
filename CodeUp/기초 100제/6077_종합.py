"""
#6077: 짝수 합 구하기
"""

"""
# 1: use 'for' to solve the problem 
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum += i

print(sum)
"""

# 2: use 'while' to solve the problem
n = int(input())
i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1

print(sum)