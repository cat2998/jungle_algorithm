import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
map = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for i in range(h)]

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

result = 0
que = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if map[i][j][k] == 1:
                que.append((i, j, k))

while que:
    i, j, k = que.popleft()
    for x, y, z in zip(dx, dy, dz):
        if 0 <= i + x < h and 0 <= j + y < n and 0 <= k + z < m and map[i + x][j + y][k + z] == 0:
            map[i + x][j + y][k + z] = map[i][j][k] + 1
            que.append((i + x, j + y, k + z))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if result != -1:
                if map[i][j][k] == 0:
                    result = -1
                    break
                result = max(result, map[i][j][k] - 1)

print(result)