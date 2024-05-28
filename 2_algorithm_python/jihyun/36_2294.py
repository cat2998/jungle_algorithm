import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for i in range(n)]
check = [0 for i in range(20001)]

que = deque()
for coin in coins:
    que.append((coin, 1))

def bfs():
    while que:
        value, cnt = que.popleft()
        if value == k:
            break
        for coin in coins:
            v = value + coin
            c = cnt + 1
            if v <= k and check[v] == 0:
                check[v] = 1
                que.append((v, c))
    
    if value != k:
        print(-1)
    else:
        print(cnt)
bfs()