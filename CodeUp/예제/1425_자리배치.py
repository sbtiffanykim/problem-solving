"""
#1425: 자리배치
"""

n, c = map(int, input().split())

heights = list(map(int, input().split()))

heights.sort()

for i in range(n):
    # 첫번째 줄에 newline이 생기는 것을 방지하기 위해 i가 0이 아니라는 조건을 추가
    if i != 0 and i % c == 0:
        print()
    print(heights[i], end=" ")
