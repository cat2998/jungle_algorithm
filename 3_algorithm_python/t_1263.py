import sys

n = int(sys.stdin.readline())
work = []
for _ in range(n):
    t, s = map(int, sys.stdin.readline().split())
    work.append((t, s))

work.sort(key=lambda x : -x[1])

end = work[0][1]
start = end - work[0][0]
for i in range(1, n):
    if start < 0:
        break
    if work[i][1] >= start:
        end = start
    else:
        end = work[i][1]
    start = end - work[i][0]

if start < 0:
    print(-1)
else:
    print(start)