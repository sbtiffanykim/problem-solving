"""
#6066: 정수 3개 입력받아 짝/홀 출력하기
"""

arr = list(map(int, input().split()))
for i in arr:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
