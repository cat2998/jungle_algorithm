import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

max_result = -sys.maxsize
min_result = sys.maxsize

def dfs(depth, total, plus, minus, mutiply, divide):
    global max_result, min_result
    if depth == n:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    else:
        if plus:
            dfs(depth + 1, total + l[depth], plus - 1, minus, mutiply, divide)
        if minus:
            dfs(depth + 1, total - l[depth], plus, minus - 1, mutiply, divide)
        if mutiply:
            dfs(depth + 1, total * l[depth], plus, minus, mutiply - 1, divide)
        if divide:
            if total < 0:
                total = -1 * total // l[depth]
                total = -1 * total
                dfs(depth + 1, total, plus, minus, mutiply, divide - 1)
            else:
                dfs(depth + 1, total // l[depth], plus, minus, mutiply, divide - 1)

dfs(1, l[0], operator[0], operator[1], operator[2], operator[3])
print(max_result)
print(min_result)