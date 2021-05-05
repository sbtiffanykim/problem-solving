import sys
from collections import deque

input = sys.stdin.readline
d = deque()

n = int(input())
for _ in range(n):
    o = input().split()
    if o[0] == "push_front":
        d.appendleft(int(o[1]))
    elif o[0] == "push_back":
        d.append(int(o[1]))
    elif o[0] == "pop_front":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif o[0] == "pop_back":
        if d:
            print(d.pop())
        else:
            print(-1)
    elif o[0] == "size":
        print(len(d))
    elif o[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif o[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif o[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)
