import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

a = "0" + a
b = "0" + b

d = [[0 for i in range(len(a))] for i in range(len(b))]

for i in range(1, len(b)):
    for j in range(1, len(a)):
        if b[i] == a[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[len(b) - 1][len(a) - 1])