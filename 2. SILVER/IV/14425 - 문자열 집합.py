import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = set()
for _ in range(n):
    S.add(input().strip())
find = list()
for _ in range(m):
    find.append(input().strip())

intersection = 0
for i in find:
    if i in S:
        intersection += 1

print(intersection)