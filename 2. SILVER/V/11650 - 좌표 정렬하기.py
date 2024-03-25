import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    num.append([x, y])

num.sort(key=lambda x : (x[0], x[1]))
for _ in range(n):
    print(num[_][0], num[_][1])