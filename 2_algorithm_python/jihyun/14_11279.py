import sys
import heapq

heap_q = []

n = int(sys.stdin.readline())

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap_q) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap_q))
    else:
        heapq.heappush(heap_q, -x)