import sys
import heapq

n = int(sys.stdin.readline())

l = []
heap_q = []
result = 0

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    l.append([min(x, y), max(x, y)])
d = int(sys.stdin.readline())

l.sort(key=lambda x : (x[1], x[0]))

for x in l:
    start, end = x[0], x[1]
    heapq.heappush(heap_q, start)
    line_start = end - d
    while heap_q and heap_q[0] < line_start:
        heapq.heappop(heap_q)
    result = max(result, len(heap_q))

print(result)