"""
#1461: 2차원 배열 순서대로 채우기 1-2
"""

n = int(input())

# 1부터 n*n까지 출력하기
for i in range(1, n + 1):
    for j in range(n):
        print(n * i - j, end=" ")
    # n개가 한 줄에 입력되면 줄바꿈하기
    print()
