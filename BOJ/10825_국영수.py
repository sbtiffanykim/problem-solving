import sys

input = sys.stdin.readline

n = int(input())
students = []

# 입력 받은 후 이름, 국어 점수, 영어 점수, 수학 점수 순서대로 튜플로 묶어 리스트에 넣기
for _ in range(n):
    info = input().split()
    students.append((info[0], int(info[1]), int(info[2]), int(info[3])))

# 여러개의 key attributes를 사용하여 우선순위를 정한다
# 국어 점수 감소 순 -> 국어 점수 같을 때 영어 점수 증가 순 -> 국어, 영어 점수가 같을 때 수학 점수 감소 순 -> 알파벳 사전 순으로 정렬
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름만 출력하기
for student in students:
    print(student[0])