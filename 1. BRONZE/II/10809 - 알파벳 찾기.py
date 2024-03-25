a = 'abcdefghijklmnopqrstuvwxyz'

b = input()

result = []

for _ in range(len(a)):
    try:
        result.append(b.index(a[_]))
    except ValueError:
        result.append(-1)

for _ in range(len(result)):
    print(result[_], end=' ')