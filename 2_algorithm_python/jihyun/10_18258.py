import sys
from queue import Queue
from collections import deque

n = int(sys.stdin.readline())

que = deque()
for i in range(n):
    st = sys.stdin.readline().split()
    if st[0] == "push":
        que.append(st[1])
    elif st[0] == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif st[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif st[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif st[0] == "size":
        print(len(que))
    elif st[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)