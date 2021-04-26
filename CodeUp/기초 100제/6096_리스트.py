"""
#6096: 바둑알 십자 뒤집기
"""

# 2차원 배열의 바둑판 입력받기
board = []
for i in range(19):
    board.append(list(map(int, input().split())))

# 십자 뒤집기 횟수 입력받기
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    # 십자 뒤집기 수행
    for k in range(19):
        # column에 대해 뒤집기 수행
        # 1이면 0으로 뒤집기
        if board[x - 1][k] == 1:
            board[x - 1][k] = 0
        # 0이면 1로 뒤집기
        else:
            board[x - 1][k] = 1

        # row에 대해 뒤집기 수행
        # 1이면 0으로 뒤집기
        if board[k][y - 1] == 1:
            board[k][y - 1] = 0
        # 0이면 1로 뒤집기
        else:
            board[k][y - 1] = 1

# 정답 출력
for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    print()