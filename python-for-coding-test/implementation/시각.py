h = int(input())

cnt = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            t = str(i) + str(j) + str(k)
            if "3" in t:
                cnt += 1

print(cnt)