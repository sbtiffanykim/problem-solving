"""
#6070: 월 입력받아 계절 출력하기
"""

m = int(input())

if m // 3 == 1:
    print("spring")
elif m // 3 == 2:
    print("summer")
elif m // 3 == 3:
    print("fall")
elif m // 3 == 4 or m // 3 == 0:
    print("winter")
