import sys

result = sys.maxsize

n = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

l.sort()

def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def get_min(start, end):

    if start == end:
        return sys.maxsize
    
    if end - start == 1:
        return get_dist(l[start], l[end])
    
    center = (start + end) // 2
    min_dist = min(get_min(start, center), get_min(center, end))

    candidates = []
    for i in range(start, end + 1):
        if (l[center][0] - l[i][0]) ** 2 < min_dist:
            candidates.append(l[i])
    
    candidates.sort(key=lambda x : x[1])

    for i in range(len(candidates) - 1):
        for j in range(i + 1, len(candidates)):
            if (candidates[i][1] - candidates[j][1]) ** 2 < min_dist:
                min_dist = min(min_dist, get_dist(candidates[i], candidates[j]))
            else:
                break
    
    return min_dist

print(get_min(0, n - 1))