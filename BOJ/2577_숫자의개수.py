a = int(input())
b = int(input())
c = int(input())
num_list = [0] * 10
n = str(a * b * c)

for i in n:
    num_list[int(i)] += 1

print(*num_list, sep="\n")