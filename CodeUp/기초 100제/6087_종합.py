"""
#6087: 3의 배수는 통과
"""

num = int(input())
i = 0

while i < num:
    i += 1
    if i % 3 != 0:
        print(i, end=" ")
    else:
        continue