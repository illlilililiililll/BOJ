import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = sorted(a-b)
print(len(result))
for i in result:
    print(i, end=' ')