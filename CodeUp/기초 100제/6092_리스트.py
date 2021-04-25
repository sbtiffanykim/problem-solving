"""
#6092: 이상한 출석 번호 부르기1
"""

n = int(input())
answer = [0] * 23
called_nums = list(map(int, input().split()))

for i in called_nums:
    answer[i - 1] += 1

for j in answer:
    print(j, end=" ")
