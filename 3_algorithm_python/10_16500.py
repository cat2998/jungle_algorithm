import sys

s = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
d = [0 for i in range(len(s) + 1)]
words = []

d[0] = 1

for i in range(n):
    words.append(sys.stdin.readline().strip())

for i in range(1, len(s) + 1):
    for word in words:
        if i >= len(word) and s[i - len(word):i] == word and d[i - len(word)] == 1:
            d[i] = 1
            break

print(d[-1])