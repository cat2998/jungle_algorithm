import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = [[] for i in range(n + 1)]
outdegree = [0 for i in range(n + 1)]
count = [0 for i in range(n + 1)]

for i in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    outdegree[y] += 1
    l[x].append((y, k))

que = deque()

que.append(n)
count[n] = 1

while que:
    top = que.popleft()
    for x in l[top]:
        count[x[0]] = count[x[0]] + count[top] * x[1]
        outdegree[x[0]] -= 1
        if outdegree[x[0]] == 0:
            que.append(x[0])

for i in range(1, n + 1):
    if len(l[i]) == 0:
        print(i, count[i])