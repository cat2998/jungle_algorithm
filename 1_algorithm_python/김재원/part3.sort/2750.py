n = int(input())
nlist = []
for i in range(n):
    nlist.append(int(input()))
nlist.sort()
for i in range(n):
    print(nlist[i])
