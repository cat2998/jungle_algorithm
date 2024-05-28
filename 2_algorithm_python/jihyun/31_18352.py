import sys
from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, sys.stdin.readline().split())
visit = [0 for i in range(n + 1)]
l = [[] for i in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)

cnt = 0
que = deque()

que.append(x)
visit[x] = 1

while que:
    x = que.popleft()
    for i in l[x]:
        if visit[i] == 0:
            visit[i] = visit[x] + 1
            if visit[i] == k + 1:
                continue
            que.append(i)

for i in range(1, n + 1):
    if visit[i] == k + 1:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)