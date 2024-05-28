import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
d = [sys.maxsize for i in range(k + 1)]

for i in range(n):
    c = int(sys.stdin.readline())
    coins.append(c)

d[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        d[i] = min(d[i], d[i - coin] + 1)

if d[k] == sys.maxsize:
    print(-1)
else:
    print(d[k])