import sys

h, min = map(int, sys.stdin.readline().split())

if min >= 45:
    min = min-45
else:
    min = 15+min
    if h == 0:
        h = 23
    else:
        h = h-1

print(h, min)