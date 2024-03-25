tot = int(input())
n = int(input())
now = 0

for i in range(n):
    price, num = map(int, input().split())
    now = now + price*num

if now == tot:
    print("Yes")
else:
    print("No")