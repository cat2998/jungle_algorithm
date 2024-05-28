import sys

k = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for i in range(k)]

stack_l = []

for i in l:
    if i == 0:
        stack_l.pop()
    else:
        stack_l.append(i)

print(sum(stack_l))