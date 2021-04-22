"""
#6081: 16진수 구구단 출력하기
"""

n = int(input(), 16)

for i in range(1, 16):
    print("%X" % n, "*", "%X" % i, "=%X" % (n * i), sep="")
    # print("%X*%X=%X" % (n, i, n * i))
