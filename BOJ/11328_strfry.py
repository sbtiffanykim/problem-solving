n = int(input())

for i in range(n):
    s1, s2 = input().split()
    if sorted(s1) == sorted(s2):
        answer = "Possible"
    else:
        answer = "Impossible"
    print(answer)