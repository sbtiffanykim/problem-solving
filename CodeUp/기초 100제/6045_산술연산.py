"""
#6045: 정수 3개 입력받아 합과 평균 출력하기
"""

a, b, c = map(int, input().split())
print(a + b + c, "%.2f" % round(((a + b + c) / 3), 2))
