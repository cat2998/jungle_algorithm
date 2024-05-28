import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
check_tree = [0 for i in range(v + 1)]
list = [[] for i in range(v + 1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    list[a].append((c, b))
    list[b].append((c, a))

heap_q = []
cnt = 0
value = 0

check_tree[1] = 1
for l in list[1]:
    if check_tree[l[1]] != 1:
        heapq.heappush(heap_q, (l[0], 1, l[1]))

while True:
    if v - 1 == cnt:
        break
    weight, a, b = heapq.heappop(heap_q)
    if check_tree[a] == 1 and check_tree[b] != 1:
        check_tree[b] = 1
        cnt += 1
        value += weight
        for l in list[b]:
            if check_tree[l[1]] != 1:
                heapq.heappush(heap_q, (l[0], b, l[1]))

print(value)