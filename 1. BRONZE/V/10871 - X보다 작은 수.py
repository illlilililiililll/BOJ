n, a = map(int, input().split())
num = list(map(int, input().split()))

for i in range(n):
    if num[i] < a:
        print(num[i], end=' ')