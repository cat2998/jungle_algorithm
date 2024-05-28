import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

a = "0" + a
b = "0" + b

d = [[0 for i in range(len(a))] for i in range(len(b))]

for i in range(1, len(b)):
    for j in range(1, len(a)):
        if a[j] == b[i]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

result = []
i = len(b) - 1
j = len(a) - 1

while True:
    if i < 1 or j < 1:
        break
    if a[j] == b[i]:
        result.append(a[j])
        i -= 1
        j -= 1
    else:
        if d[i - 1][j] > d[i][j - 1]:
            i -= 1
        else:
            j -= 1

if len(result) == 0:
    print(0)
else:
    print(len(result))
    result.reverse()
    print(*result, sep="")