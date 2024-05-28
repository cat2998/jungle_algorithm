import sys

n = int(sys.stdin.readline())
l = [sys.stdin.readline().split() for i in range(n)]

stack = []

for i in l:
    if i[0] == "push":
        stack.append(i[1])
    elif i[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
    elif i[0] == "size":
        print(len(stack))
    elif i[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())