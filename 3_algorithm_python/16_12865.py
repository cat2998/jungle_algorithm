import sys

n, k = map(int, sys.stdin.readline().split())
l = [(0, 0)]
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    l.append((w, v))

# d[i][j] = max(d[i - 1][j], d[i - 1][j -w] + v)
d = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j - l[i][0] >= 0:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - l[i][0]] + l[i][1])
        else:
            d[i][j] = d[i - 1][j]

print(d[n][k])