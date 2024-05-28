import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

tower = [(0, l[0])]
answer = [0 for i in range(n)]
for i in range(1, n):
    while answer[i] == 0:
        if len(tower) == 0:
            answer[i] = 0
            tower.append((i, l[i]))
            break
        else:
            top = tower[len(tower) - 1]
            if top[1] >= l[i]:
                answer[i] = top[0] + 1
                tower.append((i, l[i]))
            else:
                tower.pop()

for i in answer:
    print(i, end=" ")