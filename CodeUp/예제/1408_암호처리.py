"""
#1408: 암호 처리
"""

s = input()

first = list(map(lambda x: chr(ord(x) + 2), s))
second = list(map(lambda x: chr((ord(x) * 7) % 80 + 48), s))

print(*first, sep="")
print(*second, sep="")