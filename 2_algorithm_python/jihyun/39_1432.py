import sys
import heapq

n = int(sys.stdin.readline())
map = [sys.stdin.readline().strip() for i in range(n)]
l = [[] for i in range(n + 1)]
outdegree = [0 for i in range(n + 1)]
result = [0 for i in range(n + 1)]

for i in range(n):
    for j in range(n):
        if map[i][j] == '1':
            l[j + 1].append(i + 1)
            outdegree[i + 1] += 1

heap_q = []

for i in range(1, n + 1):
    if outdegree[i] == 0:
        heapq.heappush(heap_q, -1 * i)


while heap_q:
    top = -1 * heapq.heappop(heap_q)
    result[top] = n
    n -= 1
    for i in l[top]:
        outdegree[i] -= 1
        if outdegree[i] == 0:
            heapq.heappush(heap_q, -1 * i)

if sum(result) == 0:
    print(-1)
else:
    print(*result[1:])