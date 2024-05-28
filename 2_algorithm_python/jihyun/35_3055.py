import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
map = [sys.stdin.readline().strip() for i in range(r)]
fire = [[0 for i in range(c)] for i in range(r)]
hedgehog = [[0 for i in range(c)] for i in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = -1
que = deque()

for i in range(r):
    for j in range(c):
        if map[i][j] == '*':
            que.append((i, j))

while que:
    x, y = que.popleft()
    for a, b in zip(dx, dy):
        if 0 <= x + a < r and 0 <= y + b < c:
            if (map[x + a][y + b] == '.' or map[x + a][y + b] == 'S') and fire[x + a][y + b] == 0:
                fire[x + a][y + b] = fire[x][y] + 1
                que.append((x + a, y + b))

for i in range(r):
    for j in range(c):
        if map[i][j] == 'S':
            que.append((i, j))
            break

while que:
    x, y = que.popleft()
    for a, b in zip(dx, dy):
        if 0 <= x + a < r and 0 <= y + b < c and map[x + a][y + b] == 'D':
            result = hedgehog[x][y] + 1
            que.clear()
            break
        if 0 <= x + a < r and 0 <= y + b < c:
            if map[x + a][y + b] == '.' and (fire[x + a][y + b] > hedgehog[x][y] + 1 or fire[x + a][y + b] == 0) and hedgehog[x + a][y + b] == 0:
                hedgehog[x + a][y + b] = hedgehog[x][y] + 1
                que.append((x + a, y + b))

if result == -1:
    result = "KAKTUS"
print(result)