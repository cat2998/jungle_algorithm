import sys
import heapq

n = int(sys.stdin.readline())
heap_q = list(int(sys.stdin.readline()) for i in range(n))

heapq.heapify(heap_q)
result = 0

if n != 1:
    while heap_q:
        a = heapq.heappop(heap_q)
        b = heapq.heappop(heap_q)
        result += a + b
        if heap_q:
            heapq.heappush(heap_q, a + b)

print(result)