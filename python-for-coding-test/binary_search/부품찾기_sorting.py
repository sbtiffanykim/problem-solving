# counting sort 이용

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

needs = []
m = int(input())
for j in input().split():
    needs.append(j)

for j in needs:
    if array[j] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
