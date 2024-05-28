import sys
import heapq

n = int(sys.stdin.readline())

left_heap = []
right_heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -1 * x)
    else:
        heapq.heappush(right_heap, x)
    if right_heap and left_heap[0] * -1 > right_heap[0]:
        a = heapq.heappop(left_heap) * -1
        b = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -1 * b)
        heapq.heappush(right_heap, a)
    print(left_heap[0] * -1)