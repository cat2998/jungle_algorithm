import sys

st = sys.stdin.readline().strip()

tmp = 1
result = 0
stack = []

for i in range(len(st)):
    if st[i] == "(":
        stack.append("(")
        tmp *= 2
    elif st[i] == "[":
        stack.append("[")
        tmp *= 3
    elif st[i] == ")":
        if i != 0 and st[i - 1] == "(":
            result += tmp
        if len(stack) == 0:
            result = 0
            break
        p = stack.pop()
        if p != "(":
            result = 0
            break
        tmp = tmp // 2
    elif st[i] == "]":
        if i != 0 and st[i - 1] == "[":
            result += tmp
        if len(stack) == 0:
            result = 0
            break
        p = stack.pop()
        if p != "[":
            result = 0
            break
        tmp = tmp // 3
    
if len(stack) != 0:
    result = 0

print(result)