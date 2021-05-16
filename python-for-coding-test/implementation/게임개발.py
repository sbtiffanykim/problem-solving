n, m = int(input().split())
x, y, direction = int(input().split())

# 방문 여부를 기록하기 위한 list
vis = [[0] * m for _ in range(n)]
vis[x][y] = 1

# 맵 입력받기
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 북, 동, 남, 서 이동 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    # 북, 동, 남, 서 방향으로 되어있으므로 왼쪽으로 돌면 하나씩 감소
    direction -= 1
    # 범위 벗어나면 서쪽으로 설정
    if direction == -1:
        direction = 3


# 방문한 칸의 수를 저장하기 위한 변수
cnt = 1
# 왼쪽으로 회전하는 횟수 저장하기 위한 변수
# 네 방향이 모두 진행 불가 지역일 때를 계산하기 위해 설정
turn_time = 0

while True:
    # 1번 - 왼쪽으로 회전하고 갈 곳을 정하기
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 2번 - 바다가 아니고 방문하지 않은 경우 이동한 후 해당 칸 방문 처리한 후 1번부터 시작
    if board[nx][ny] == 0 and vis[nx][ny] == 0:
        vis[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        continue
    # 2번 - 회전한 후 가보지 않은 칸이 없다면 왼쪽으로 회전만 수행
    else:
        turn_time += 1

    # 3번 - 네 방향 모두 갈 수 없는 경우 한칸 뒤로 이동
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒷쪽이 바다가 아닌 경우 뒤로 이동
        if board[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우 움직임을 멈춘다
        else:
            break
        # 3번까지 시행 후 다시 1단계로 돌아가므로 turn_time을 1로 초기화
        turn_time = 0

# 정답 출력
print(cnt)