import sys

n = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
marble = list(map(int, sys.stdin.readline().split()))

weight = [ 0 ]
for w in tmp:
    t = len(weight)
    for i in range(t):
        weight.append(weight[i] + w)
        weight.append(abs(weight[i] - w))
    weight = list(set(weight))

for i in marble:
    if i not in weight:
        print("N", end=" ")
    else:
        print("Y", end=" ")