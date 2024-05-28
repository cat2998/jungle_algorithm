import sys

n, k = map(int, sys.stdin.readline().split())
product = list(map(int, sys.stdin.readline().split()))
plug = [0 for _ in range(n)]

plug[0] = product[0]
for i in range(1, n):
    for j in range(i, k):
        if product[j] not in plug:
            plug[i] = product[j]
            break

if plug[n - 1] == 0:
    print(0)
    exit()

cnt = 0
for i in range(k):
    if product[i] in plug:
        continue
    else:
        tmp = [sys.maxsize for i in range(n)]
        for j in range(i + 1, k):
            for p in range(n):
                if product[j] == plug[p] and tmp[p] == sys.maxsize:
                    tmp[p] = j
                    break
        
        max_tmp = -sys.maxsize
        max_idx = 0
        flag = 1
        for t in range(n):
            if max_tmp < tmp[t]:
                max_tmp = tmp[t]
                max_idx = t

        cnt += 1
        plug[max_idx] = product[i]

print(cnt)