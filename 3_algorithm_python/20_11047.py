import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
result = 0

for i in range(n):
    coins.append(int(sys.stdin.readline()))

for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if k // coins[i] == 0 and k < coins[i]:
        continue
    else:
        result += k // coins[i]
        k = k % coins[i]

print(result)