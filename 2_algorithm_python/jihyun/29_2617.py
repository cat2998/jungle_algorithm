import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
heavy_list = [[] for i in range(n + 1)]
light_list = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    heavy_list[a].append(b)
    light_list[b].append(a)

result = 0

def dfs(array, node):
    cnt = 0
    for i in array[node]:
        if visit[i] == 0:
            visit[i] = 1
            cnt += 1
            cnt += dfs(array, i)
    return cnt

for i in range(1, n + 1):
    visit = [0 for i in range(n + 1)]
    cnt = dfs(heavy_list, i)
    if cnt > n // 2:
        result += 1
    cnt = dfs(light_list, i)
    if cnt > n // 2:
        result += 1

print(result)