import sys
import heapq

n = int(sys.stdin.readline())
questions = [[] for i in range(n + 1)]

for i in range(n):
    limit, value = map(int, sys.stdin.readline().split())
    questions[limit].append(value)

heap_q = []
value = 0

for i in range(n, 0, -1):
    if questions[i]:
        ls = questions[i]
        for l in ls:
            heapq.heappush(heap_q, -l)
    if heap_q:
        value += -heapq.heappop(heap_q)

print(value)