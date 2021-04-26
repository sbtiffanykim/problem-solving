"""
#6097: 설탕과자 뽑기
"""

h, w = map(int, input().split())
# 격자판을 0으로 초기화
board = [[0] * w for i in range(h)]

n = int(input())
for i in range(1, n + 1):
    l, d, x, y = map(int, input().split())
    # board[0][0]부터 시작하므로 1을 빼줌
    x -= 1
    y -= 1

    # 가로로 배치하는 경우
    if d == 0:
        for k in range(l):
            board[x][y + k] = 1

    # 세로로 배치하는 경우
    else:
        for k in range(l):
            board[x + k][y] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end=" ")
    print()