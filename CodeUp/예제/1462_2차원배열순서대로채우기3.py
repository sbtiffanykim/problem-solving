"""
#1462: 2차원 배열 순서대로 채우기 1-3
"""

n = int(input())

# 1부터 n*n까지 출력하기
for i in range(1, n + 1):
    for j in range(0, n):
        print(n * j + i, end=" ")
    # n개가 한 줄에 입력되면 줄바꿈하기
    print()
