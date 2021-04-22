"""
#6067: 정수 1개 입력받아 분류하기
"""

n = int(input())
if n > 0:
    if n % 2 == 0:
        print("C")
    else:
        print("D")

else:
    if n % 2 == 0:
        print("A")
    else:
        print("B")
