"""
#6095: 바둑판에 흰 돌 놓기
"""

# 바둑판 초기화
board = [[0] * 19 for _ in range(19)]
n = int(input())

# 흰돌 표시
for i in range(n):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    # 줄바꿈
    print()