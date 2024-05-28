import sys

n = int(sys.stdin.readline())

l = []
stack = []
cnt = 1

for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    l.append([x - r, 0])
    l.append([x + r, 1])

l.sort(key = lambda x : (x[0], -x[1]))

for x, shape in l:
    len = 0
    if shape == 0:
        stack.append([x, 0])
    else:
        top, len = stack.pop()
        cnt += 1
        if stack:
            stack[-1][1] += x - top
        if x - top == len:
            cnt += 1

print(cnt)