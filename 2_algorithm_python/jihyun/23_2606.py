import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = [[] for i in range(n + 1)]
visit = [0 for i in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

cnt = 0
que = deque()

que.append(1)
visit[1] = 1
while que:
    top = que.popleft()
    cnt += 1
    for i in l[top]:
        if visit[i] == 0:
            visit[i] = 1
            que.append(i)

print(cnt - 1)