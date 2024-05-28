import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for i in range(n)]

top = 0
result = 0
for i in range(len(l)):
    p = l.pop()
    if top < p:
        top = p
        result += 1

print(result)