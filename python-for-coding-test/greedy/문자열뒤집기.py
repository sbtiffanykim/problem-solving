s = input()

zeros = [j for j in range(len(s)) if s[j] != "1"]
ones = [i for i in range(len(s)) if s[i] != "0"]

prev = zeros[0]
print(zeros)
count = 1
for i in range(1, len(zeros)):
    if zeros[i] == prev + 1:
        prev = zeros[i]
    else:
        print(zeros[i])
        count += 1
        prev = zeros[i]

print(count)
# print(t)
