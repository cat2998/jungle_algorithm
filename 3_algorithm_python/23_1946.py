import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    ranks = []
    
    for j in range(n):
        rank1, rank2 = map(int, sys.stdin.readline().split())
        ranks.append((rank1, rank2))
    
    ranks.sort()

    top = ranks[0][1]
    cnt = 1

    for i in range(1, n):
        if top > ranks[i][1]:
            top = ranks[i][1]
            cnt += 1
        
    
    print(cnt)