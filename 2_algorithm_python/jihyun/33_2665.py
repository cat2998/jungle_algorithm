import sys
from collections import deque

n = int(sys.stdin.readline())
map = [sys.stdin.readline().strip() for i in range(n)]
broken = [[sys.maxsize for i in range(n)] for i in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

que = deque()

que.append((0,0))
broken[0][0] = 0

while que:
    x, y = que.popleft()
    for a, b in zip(dx, dy):
        if 0 <= x + a < n and 0 <= y + b < n and broken[x][y] < broken[x + a][y + b]:
            if map[x + a][y + b] == '0':
                broken[x + a][y + b] = min(broken[x + a][y + b], broken[x][y] + 1)
            else:
                broken[x + a][y + b] = min(broken[x + a][y + b], broken[x][y])
            que.append((x + a, y + b))

print(broken[n - 1][n - 1])