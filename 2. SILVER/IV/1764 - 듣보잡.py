import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set()
see = set()
for _ in range(n):
    listen.add(input().strip())
for  _ in range(m):
    see.add(input().strip())

all = sorted(listen & see)
print(len(all))
for i in all:
    print(i)