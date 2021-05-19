import sys

sys.setrecursionlimit(10 ** 6 + 1)


input = sys.stdin.readline


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
store = list(map(int, input().split()))
m = int(input())
items = list(map(int, input().split()))

store.sort()

for i in items:
    result = binary_search(store, i, 0, n - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
