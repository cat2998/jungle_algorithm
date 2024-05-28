import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = [[] for i in range(n + 1)]
for i in range(1, m + 1):
    a, b, v = map(int, sys.stdin.readline().split())
    l[a].append([b, v]) 
start, end = map(int, sys.stdin.readline().split())
d = [sys.maxsize for i in range(n + 1)]

que = deque()

d[start] = 0
que.append((0, start))
while que:
    value, p = que.popleft()
    if d[p] != value:
        continue
    for i in l[p]:
        if d[i[0]] > value + i[1]:
            d[i[0]] = value + i[1]
            que.append((d[i[0]], i[0]))

print(d[end])