import sys

t = int(sys.stdin.readline())
k = int(sys.stdin.readline())

d = [0 for i in range(t + 1)]
coins = []

for i in range(k):
    p, n = map(int, sys.stdin.readline().split())
    coins.append((p, n))

d[0] = 1

for coin, cnt in coins:
    for i in range(t, coin - 1, -1):
        for c in range(1, cnt + 1):
            if i - coin * c >= 0:
                d[i] += d[i - coin * c]

print(d[t])