"""
#6056: 참/거짓이 서로 다를 때에만 참 출력하기
"""

a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print((not a and b) or (a and not b))