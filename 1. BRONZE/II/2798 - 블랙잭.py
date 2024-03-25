import sys
input = sys.stdin.readline

n, target = map(int, input().split())
l = list(map(int, input().split()))
max = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if l[i]+l[j]+l[k] >= max and l[i]+l[j]+l[k] <= target:
                max = l[i]+l[j]+l[k]

print(max)