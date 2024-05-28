import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
l = [[] for i in range(n + 1)]
indegree = [0 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    indegree[b] += 1

que = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    top = que.popleft()
    print(top, end=" ")
    for i in l[top]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)