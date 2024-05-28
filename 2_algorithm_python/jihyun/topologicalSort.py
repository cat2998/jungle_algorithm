import sys
from collections import deque

n = int(sys.stdin.readline())
l = [[] for i in range(n + 1)]

que = deque()
indegree = [0 for i in range(n + 1)]

for i in range(n):
    a, b = sys.stdin.readline().split()
    l[ord(a) - 65 + 1].append(ord(b) - 65 + 1)
    indegree[ord(b) - 65 + 1] += 1

print(l)
print(indegree)

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    top = que.popleft()
    print(chr(top -1 + 65))
    for i in l[top]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)