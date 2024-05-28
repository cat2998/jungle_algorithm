import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = [[] for i in range(n + 1)]
indegree = [0 for i in range(n + 1)]
time = [0 for i in range(n + 1)]
road = [[] for i in range(n + 1)]

for i in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    l[s].append((e, t))
    indegree[e] += 1

start, end = map(int, sys.stdin.readline().split())

que = deque()
que.append(start)

while que:
    top = que.popleft()
    for nxt, value in l[top]:
        if time[nxt] < time[top] + value:
            road[nxt] = [top]
            time[nxt] = time[top] + value
        elif time[nxt] == time[top] + value:
            road[nxt].append(top)
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            que.append(nxt)

q = deque([end])
route = set()
while q:
    now = q.popleft()
    for x in road[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(time[end])
print(len(route))