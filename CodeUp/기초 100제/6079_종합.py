"""
#6079: 정수 1개 입력받아 그 수까지 출력하기2
"""

n = int(input())

s = 0
i = 1
while True:
    s += i
    if s > n:
        break
    i += 1
    print(f"sum: {s} idx: {i}")

print(i - 1)
