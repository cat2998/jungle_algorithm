import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d = [0 for i in range(n)]
d[0] = 1

for i in range(1, n):
    max_d = 0
    for j in range(i):
        if a[j] < a[i]:
            max_d = max(max_d, d[j])
    d[i] = max_d + 1

max_d = 0
for i in range(n):
    max_d = max(max_d, d[i])

print(max_d)