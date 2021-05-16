# 현재 나이트의 위치 입력받기
curr = input()
curr_x = ord(curr[0]) - ord("a") + 1
curr_y = int(curr[1])

# 나이트가 이동할 수 있는 방향 정의
dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

# 이동 가능 횟수를 저장하기 위한 변수 설정
cnt = 0

# 8개의 밤향에 대해 이동 가능성 확인
for i in range(8):
    nx = curr_x + dx[i]
    ny = curr_y + dy[i]
    # 만약 8x8의 board 범위를 벗어난다면 나이트는 이동 가능하지 않다
    if nx >= 8 or ny >= 8 or nx < 1 or ny < 1:
        continue
    else:
        cnt += 1

print(cnt)
