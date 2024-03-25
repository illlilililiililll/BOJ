n, m = map(int, input().split())

basket = []

for _ in range(1, n+1):
    basket.append(_)

for _ in range(m):
    i, j= map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for _ in range(n):
    print(basket[_], end=' ')