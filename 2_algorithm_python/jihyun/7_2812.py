import sys

n, k = map(int, sys.stdin.readline().split())
numbers = sys.stdin.readline().strip()

cnt = 0
stack = []

for number in numbers:
    while len(stack) != 0 and stack[-1] < number and cnt < k:
        stack.pop()
        cnt += 1
    stack.append(number)

for i in range(n - k):
    print(stack[i], end="")