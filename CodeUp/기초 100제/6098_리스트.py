"""
#6098: 성실한 개미
"""

# 길 입력받기
board = []
for _ in range(10):
    board.append(list(map(int, input().split())))

# 이동
def move(x, y):

    while board[x][y] != 2:
        if board[x][y + 1] != 1:
            ny = y + 1

        else:
            nx = x + 1

        if nx >= 10 or ny >= 10:
            continue

        x = nx
        y = ny

        board[x][y] = 9


# 출발
x = 1
y = 1
board[x][y] = 9

move(x, y)

board[x][y] = 9


# 정답 출력
for i in range(10):
    for j in range(10):
        print(board[i][j], end=" ")
    print()