import sys

s = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
marble = list(map(int, sys.stdin.readline().split()))

cnt = 1
stones = []
for i in range(0, len(tmp) - 1):
    if tmp[i] != tmp[i + 1]:
        stones.append((tmp[i], cnt))
        cnt = 1
        if i == len(tmp) - 2:
            stones.append((tmp[i + 1], cnt))
    else:
        cnt += 1
        if i == len(tmp) - 2:
            stones.append((tmp[i], cnt))

if len(tmp) == 1:
    stones.append((tmp[0], 1))

d = [0 for i in range(sum(tmp) + 1)]
d[0] = 1

for stone, cnt in stones:
    for i in range(len(d) - 1, 0, -1):
        for c in range(1, cnt + 1):
            if i - stone * c >= 0:
                d[i] += d[i - stone * c]

for stone, cnt in stones:
    for i in range(1, len(d) + 1):
        for c in range(1, cnt + 1):
            if i + stone * c < len(d):
                d[i] += d[i + stone * c]

for i in marble:
    if i >= len(d) or d[i] == 0:
        print("N", end=" ")
    else:
        print("Y", end=" ")