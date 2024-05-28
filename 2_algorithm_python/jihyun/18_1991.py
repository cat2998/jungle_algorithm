import sys

n = int(sys.stdin.readline())

lc = [0 for i in range(n)]
rc = [0 for i in range(n)]

for i in range(n):
    v, l, r = sys.stdin.readline().split()
    if l != '.':
        lc[ord(v) - 65] = ord(l) - 65
    if r != '.':
        rc[ord(v) - 65] = ord(r) - 65

def preorder(cur):
    print(chr(cur + 65), end="")
    if lc[cur] != 0:
        preorder(lc[cur])
    if rc[cur] != 0:
        preorder(rc[cur])

def inorder(cur):
    if lc[cur] != 0:
        inorder(lc[cur])
    print(chr(cur + 65), end="")
    if rc[cur] != 0:
        inorder(rc[cur])

def postorder(cur):
    if lc[cur] != 0:
        postorder(lc[cur])
    if rc[cur] != 0:
        postorder(rc[cur])
    print(chr(cur + 65), end="")

preorder(0)
print("")
inorder(0)
print("")
postorder(0)