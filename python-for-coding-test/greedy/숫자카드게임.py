# 각 행에서 가장 작은 수를 골라 그 중에서 가장 큰 수를 뽑기
n, m = map(int, input().split())
nums = []

for i in range(n):
    t = list(map(int, input().split()))
    nums.append(min(t))

print(max(nums))