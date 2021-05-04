import sys

stack = []
input = sys.stdin.readline
n = int(input())

for i in range(n):
    o = list(map(str, input().split()))
    if o[0] == "push":
        stack.append(int(o[1]))
    elif o[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif o[0] == "size":
        print(len(stack))

    elif o[0] == "pop":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)

    elif o[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
