import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]
d = [[-1]*n for i in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if d[x][y] == -1:
        d[x][y] = 0
        for i in range(4):
            dr_x, dr_y = x + dx[i], y + dy[i]
            if 0 <= dr_x < m and 0 <= dr_y < n and arr[dr_x][dr_y] < arr[x][y]:
                d[x][y] += dfs(dr_x, dr_y)
    return d[x][y]

print(dfs(0, 0))