import sys
from collections import deque

n = int(sys.stdin.readline())
l = [[] for i in range(n + 1)]
parent = [-1 for i in range(n + 1)]

for i in range(1, n):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

que = deque()

que.append(1)
parent[1] = 1
while que:
    top = que.popleft()
    for i in l[top]:
        if parent[i] == -1:
            parent[i] = top
            que.append(i)

print(*parent[2:], sep="\n")