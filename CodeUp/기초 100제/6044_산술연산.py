"""
#6044: 정수 2개 입력받아 자동 계산하기
"""

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print("%.2f" % float(a / b))
