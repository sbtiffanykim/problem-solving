s = input()
letters = []

for i in range(26):
    n = s.count(chr((ord("a") + i)))
    letters.append(n)

print(*letters, sep=" ")