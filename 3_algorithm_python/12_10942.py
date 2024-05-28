import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
questions = []

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    questions.append((s, e))

num = [0] + num
map = [[0 for i in range(n + 1)] for i in range(n + 1)]
map[n][n] = 1

for i in range(n - 1, 0, -1):
    for j in range(1, n + 1):
        if i == j:
            map[i][j] = 1
        if map[i + 1][j - 1] == 1 or i + 1 == j:
            if num[i] == num[j]:
                map[i][j] = 1

for i, j in questions:
    print(map[i][j])