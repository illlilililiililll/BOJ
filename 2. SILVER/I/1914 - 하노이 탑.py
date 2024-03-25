def hanoi(n, start, end, mid):
    if n == 0:
        return
    hanoi(n-1, start, mid, end)
    print(start, end)
    hanoi(n-1, mid, end, start)

n = int(input())
if n > 20:
    print(2**n-1)
else:
    print(2**n-1)
    hanoi(n, 1, 3, 2)