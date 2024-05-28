# 1992 : 쿼드트리
import sys

n = int(sys.stdin.readline())
l = [sys.stdin.readline().strip() for i in range(n)]

def is_pack(n, x, y):
    for i in range(n):
        for j in range(n):
            if l[x][y] != l[x + i][y + j]:
                return -1
    return int(l[x][y])

def div(n, x, y):
    pack = is_pack(n, x, y)

    if n == 2:
        if pack == -1:
            print("("+l[x][y]+l[x][y + 1]+l[x + 1][y]+l[x + 1][y + 1]+")", end="")
        else:
            print(pack, end="")

    else:
        if pack == -1:
            print("(", end="")
            div(n//2, x, y)
            div(n//2, x, y + n//2)
            div(n//2, x + n//2, y)
            div(n//2, x + n//2, y + n//2)
            print(")", end="")
        else:
            print(pack, end="")

div(n, 0, 0)