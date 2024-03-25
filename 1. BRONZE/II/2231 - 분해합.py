n = int(input())

i = 0
while True:
    if i >= n:
        print(0)
        break
    a = 0
    for _ in range(len(str(i))):
        a += int(str(i)[_])
    a += i
    if a == n:
        print(i)
        break
    i += 1