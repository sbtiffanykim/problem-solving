n = int(input())
result = 0
nums = []

for i in range(n):
    t = int(input())
    if t > 0:
        nums.append(t)
    else:
        nums.pop()

print(sum(nums))