import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

d = [0 for i in range(n + 1)]
vip = [0 for i in range(n + 1)]

for _ in range(m):
    v = int(sys.stdin.readline())
    vip[v] = 1

d[0] = d[1] = 1

# d[i] = d[i - 1] + d[i - 2]
for i in range(2, n + 1):
    if vip[i] or vip[i - 1]:
        d[i] = d[i - 1]
    else:
        d[i] = d[i - 1] + d[i - 2]

print(d[n])