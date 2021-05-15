from itertools import permutations

n = int(input())
nums = [i for i in range(1, n + 1)]
perlist = list(permutations(nums, n))


for i in perlist:
    print(*i, sep=" ")
