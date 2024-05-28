import sys

n, m = map(int, sys.stdin.readline().split())
map = [sys.stdin.readline().strip() for i in range(n)]
visit = [[0 for i in range(m)] for i in range(n)]

def dfs(x, y):
    visit[x][y] = 1
    if map[x][y] == '-':
        if y + 1 < m and map[x][y + 1] == '-':
            dfs(x, y + 1)
    else:
        if x + 1 < n and map[x + 1][y] == '|':
            dfs(x + 1, y)
    return

cnt = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            cnt += 1
            dfs(i, j)

print(cnt)