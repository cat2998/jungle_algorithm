import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
st = "0" + sys.stdin.readline().strip()
inout = [int(i) for i in st]
visit = [0 for i in range(n + 1)]
l = [[] for i in range(n + 1)]

answer = 0
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)
    if inout[a] == 1 and inout[b] == 1:
        answer += 2

def dfs(node):
    cnt = 0
    visit[node] = 1
    for i in l[node]:
        if inout[i] == 1:
            cnt += 1
        elif visit[i] == 0 and inout[i] == 0:
            cnt += dfs(i)
    return cnt

for i in range(1, n + 1):
    if visit[i] == 0 and inout[i] == 0:
        cnt = dfs(i)
        answer = answer + cnt * (cnt - 1)

print(answer)