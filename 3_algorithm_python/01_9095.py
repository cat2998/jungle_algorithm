import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    d = [0 for i in range(n + 1)]
    
    d[0] = d[1] = 1
    if n >= 2:
        d[2] = 2
    
    for i in range(3, n + 1):
        d[i] += d[i - 1] + d[i - 2] + d[i - 3]
    
    print(d[n])