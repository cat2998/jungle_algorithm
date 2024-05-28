import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
visit = [0 for i in range(n + 1)]
l = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

cnt = 0
que = deque()

for i in range(1, n + 1):
    if visit[i] == 0:
        que.append(i)
        visit[i] = 1
        cnt += 1
        while que:
            top = que.popleft()
            for j in l[top]:
                if visit[j] == 0:
                    visit[j] = 1
                    que.append(j)

print(cnt)