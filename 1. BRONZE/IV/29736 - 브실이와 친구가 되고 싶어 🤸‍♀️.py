import sys
input = sys.stdin.readline

a, b = map(int, input().split())
k, x = map(int, input().split())

friend = [i for i in range(a, b+1)]
count = 0
for i in range(k-x, k+x+1):
    if i in friend:
        count += 1
if count == 0:
    print('IMPOSSIBLE')
else:
    print(count)