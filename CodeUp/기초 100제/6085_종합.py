"""
#6084: 그림 파일 저장용량 계산하기
"""

w, h, b = map(int, input().split())

print("%.2f" % (w * h * b / 8 / 1024 / 1024), "MB")
