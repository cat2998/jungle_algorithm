import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
visit = [0 for i in range(n + 1)]
l = [[] for i in range(n + 1)]

stack = []
queue = deque()

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)
    l[a].sort()
    l[b].sort()

def bfs_init():
    for i in range(n + 1):
        visit[i] = 0

def dfs_not_recursion():
    stack.append(v)
    while stack:
        top = stack.pop()
        if visit[top] == 0:
            print(top, end=" ")
        visit[top] = 1
        for node in l[top]:
            if visit[node] == 0:
                stack.append(node)

def dfs(cur):
    visit[cur] = 1
    print(cur, end=" ")
    for node in l[cur]:
        if visit[node] == 0:
            dfs(node)

def bfs():
    queue.append(v)
    visit[v] = 1
    while queue:
        top = queue.popleft()
        print(top, end=" ")
        for node in l[top]:
            if visit[node] == 0:
                visit[node] = 1
                queue.append(node)

dfs(v)
bfs_init()
print()
bfs()