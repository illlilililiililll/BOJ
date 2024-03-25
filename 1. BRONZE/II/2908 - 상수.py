a, b = map(list, input().split())
a.reverse()
a = int(''.join(a))
b.reverse()
b = int(''.join(b))

if a > b:
    print(a)
else:
    print(b)