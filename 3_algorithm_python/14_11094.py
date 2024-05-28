import sys

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    matrix.append((r, c))

def matrix_multi(a, b):
    a_r, a_c, a_cnt = a[0], a[1], a[2]
    b_r, b_c, b_cnt = b[0], b[1], b[2]
    if a_r == b_r:
        result = (a_c, b_c, a_cnt + b_cnt + a_c * a_r * b_c)
    else:
        result = (a_c, b_r, a_cnt + b_cnt + a_c * a_r * b_r)
    return result


d = [[(0, 0, 0) for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            d[i][j] = (matrix[i][0], matrix[i][1], 0)
        if j == i - 1:
            print(j, i)
            d[i][j] = matrix_multi


print(*d, sep="\n")

for j in range(n):
    for i in range(n):
        if j < i - 1:
            # print(j, i, end=" ")
            print(j, i)
            # for k in range(i):
            #     print()