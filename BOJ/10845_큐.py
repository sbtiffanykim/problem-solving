from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    o = input().split()
    if o[0] == "push":
        queue.append(int(o[1]))
    elif o[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif o[0] == "size":
        print(len(queue))
    elif o[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif o[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif o[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
