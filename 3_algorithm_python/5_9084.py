import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    d = [0 for i in range(m + 1)]

    d[0] = 1
    for coin in coins:
        for j in range(coin, m + 1):
            d[j] += d[j - coin]

    print(d[m])