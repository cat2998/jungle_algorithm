import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
dummy = [[0 for i in range(n)] for i in range(n)]
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    dummy[a - 1][b - 1] = 1
l = int(sys.stdin.readline())
l_list = [sys.stdin.readline().split() for i in range(l)]

time = 0
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 오른쪽, 아래, 왼쪽, 위
d = 0
l_idx = 0

deq = deque([[0,0]])

while True:
    start = deq[0]
    x, y = tuple(sum(i) for i in zip(start, directions[d]))
    time += 1
    if not(0 <= x <= n - 1 and 0 <= y <= n - 1) or deq.count([x, y]) > 0:
        break
    deq.appendleft([x, y])
    if dummy[x][y] == 1:
        dummy[x][y] = 0
    else:
        deq.pop()
    for i in range(l_idx, l):
        if int(l_list[i][0]) == time:
            if l_list[i][1] == "D":
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4
            l_idx += 1

print(time)