import sys
sys.setrecursionlimit(10 ** 5)

t = int(sys.stdin.readline())
for i in range(t):
    v, e = map(int, sys.stdin.readline().split())
    l = [[] for i in range(v + 1)]
    visit = [-1 for i in range(v + 1)]
    flag = 0

    for j in range(e):
        a, b = map(int, sys.stdin.readline().split())
        l[a].append(b)
        l[b].append(a)
    
    def dfs(node, num):
        global flag
        visit[node] = num % 2
        for n in l[node]:
            if visit[n] == num % 2:
                flag = 1
                break
            if visit[n] == -1:
                dfs(n, num + 1)
    
    if v == 1:
        print("NO")
        continue
    
    for j in range(1, v + 1):
        if visit[j] == -1:
            dfs(j, 0)
    
    print("NO" if flag else "YES")