import sys

n = int(sys.stdin.readline())

# d[i] = d[i - 1] + d[i - 2]
d = [0 for i in range(n + 1)]
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 15746
    print(d[n])