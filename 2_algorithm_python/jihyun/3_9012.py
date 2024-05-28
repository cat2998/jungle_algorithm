import sys

t = int(sys.stdin.readline())
l = [sys.stdin.readline().strip() for i in range(t)]

for i in l:
    flag = 1
    stack = []
    for j in range(len(i)):
        if i[j] == "(":
            stack.append(1)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                flag = 0
    if flag == 0 or len(stack) != 0:
        print("NO")
    else:
        print("YES")