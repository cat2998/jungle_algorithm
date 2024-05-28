import sys
import heapq

n = int(sys.stdin.readline())
classes = []
heap_q = []

for i in range(n):
    number, start, end = map(int, sys.stdin.readline().split())
    classes.append((start, end))

classes.sort()
result = 0

for c in classes:
    start, end = c
    while heap_q and heap_q[0] <= start:
        heapq.heappop(heap_q)
    heapq.heappush(heap_q, end)
    result = max(result, len(heap_q))

print(result)