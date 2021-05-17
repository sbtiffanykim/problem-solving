s = input()
answer = []
nums = []

for i in s:
    if ord(i) >= ord("1") and ord(i) <= ord("9"):
        nums.append(int(i))
    else:
        answer.append(i)

answer.sort()
answer.append(sum(nums))
print(*answer, sep="")