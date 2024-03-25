n, m = map(int, input().split())

basket = []

for _ in range(n):
    basket.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())

    for a in range(i-1, j):
        basket[a] = k

for _ in range(n):
    print(basket[_], end=' ')