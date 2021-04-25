"""
#6094: 이상한 출석 번호 부르기3
"""

n = int(input())
called_nums = list(map(int, input().split()))

print(min(called_nums))

# min_num = called_nums[0]
# for i in range(1, n):
#     if called_nums[i] < min_num:
#         min_num = called_nums[i]

# print(min_num)