import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map = [sys.stdin.readline().strip() for i in range(m)]
visit = [[0 for i in range(n)] for i in range(m)]

# print(map)
# print(visit)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

w_cnt = 0
m_cnt = 0

que = deque()

for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            que.append((i, j))
            visit[i][j] = 1
            cnt = 1
            while que:
                x, y = que.popleft()
                for a, b in zip(dx, dy):
                    if 0 <= x + a < m and 0 <= y + b < n and visit[x + a][y + b] == 0 and map[x + a][y + b] == map[x][y]:
                        visit[x + a][y + b] = 1
                        cnt += 1
                        que.append((x + a, y + b))
            if map[i][j] == 'W':
                w_cnt += cnt ** 2
            else:
                m_cnt += cnt ** 2

print(w_cnt)
print(m_cnt)