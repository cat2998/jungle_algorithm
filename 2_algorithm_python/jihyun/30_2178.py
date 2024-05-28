import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().strip()) for i in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

que = deque()

def bfs():
    que.append((0, 0))
    map[0][0] = 2
    while que:
        a, b = que.popleft()
        for x, y in zip(dx, dy):
            if 0 <= a + x < n and 0 <= b + y < m and map[a + x][b + y] == '1':
                map[a + x][b + y] = map[a][b] + 1
                que.append((a + x, b + y))

bfs()
print(map[n - 1][m - 1] - 1)