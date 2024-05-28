import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
year = 0
que = deque()

def dfs(a, b):
    visit[a][b] = 1
    for x, y in zip(dx, dy):
        if 0 <= a + x < n and 0 <= b + y < m and map[a + x][b + y] != 0 and visit[a + x][b + y] == 0:
            dfs(a + x, b + y)

while True:
    visit = [[0 for i in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                que.append((i, j))

    if len(que) == n * m:
        year = 0
        break

    while que:
        a, b = que.popleft()
        for x, y in zip(dx, dy):
            if 0 <= a + x < n and 0 <= b + y < m and map[a + x][b + y] != 0:
                map[a + x][b + y] -= 1
    # print()
    # print(*map, sep="\n")

    cnt = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] != 0 and visit[i][j] == 0:
                dfs(i, j)
                cnt += 1
    
    # print(cnt)
    # print()
    # print(*visit, sep="\n")
    year += 1

    if cnt > 1:
        break

print(year)