"""
#1463: 2차원 배열 순서대로 채우기 1-4
"""

n = int(input())

# 1부터 n*n까지 출력하기
for i in range(n, 0, -1):
    for j in range(n):
        print(n * j + i, end=" ")
    # n개가 한 줄에 입력되면 줄바꿈하기
    print()
