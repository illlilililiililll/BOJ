import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = dict()
for _ in range(n):
    site, pw = input().split()
    data[site] = pw

for _ in range(m):
    print(data[input().strip()])