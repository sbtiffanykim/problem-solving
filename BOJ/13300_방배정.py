import math

n, k = map(int, input().split())
students = [[0] * 6 for _ in range(2)]

# 입력받고 성별 & 학년대로 분류하기
for i in range(n):
    s, y = map(int, input().split())
    students[s][y - 1] += 1

rooms = 0
for s in range(2):
    for y in range(6):
        # 성별, 학년별로 필요한 방의 개수 구하기
        # k로 나눴을 때의 값이 flaot이면 무조건 방이 하나 더 필요하므로 math.ceil이용
        rooms += math.ceil(students[s][y] / k)

print(rooms)