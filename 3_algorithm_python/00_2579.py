import sys

n = int(sys.stdin.readline())
step = [0 for _ in range(n)]
d = [0 for _ in range(n)]

for i in range(n):
    step[i] = int(sys.stdin.readline())

d[0] = step[0]
if n >= 2:
    d[1] = step[0] + step[1]
if n >= 3:
    d[2] = max(step[0] + step[2], step[1] + step[2])

# d[i] = max(d[i - 3] + step[i - 1] + step[i], d[i - 2] + step[i])
for i in range(3, n):
    d[i] = max(d[i - 3] + step[i - 1] + step[i], d[i - 2] + step[i])

print(d[n - 1])