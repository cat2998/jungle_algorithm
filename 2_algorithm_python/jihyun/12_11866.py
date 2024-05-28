import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

deq = deque([i for i in range(1, n + 1)])
result = []

while len(deq) != 0:
    deq.rotate(-(k - 1))
    result.append(deq.popleft())

print("<", end="")
print(*result, sep=', ', end='')
print(">", end="")