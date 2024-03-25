n = int(input())

num = []

for _ in range(n):
    new = int(input())
    if new == 0:
        num.pop()
        continue
    num.append(new)

print(sum(num))