import sys

n = int(sys.stdin.readline())
times = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    times.append([s, e])

times.sort(key=lambda x : (x[1], x[0]))

cnt = 1
curr = times[0][1]
for i in range(1, n):
    if curr <= times[i][0]:
        curr = times[i][1]
        cnt += 1

print(cnt)