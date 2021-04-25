"""
#6093: 이상한 출석 번호 부르기2
"""

n = int(input())
called_nums = list(map(int, input().split()))

for j in range(n - 1, -1, -1):
    print(called_nums[j], end=" ")

# called_nums.reverse()