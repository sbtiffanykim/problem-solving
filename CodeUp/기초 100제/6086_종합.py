"""
#6086: 거기까지! 이제 그만~
"""

num = int(input())
idx = 1
total = 0

while True:
    total += idx
    idx += 1
    if total >= num:
        break

print(total)
