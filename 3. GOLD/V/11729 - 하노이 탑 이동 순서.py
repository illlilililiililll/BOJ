n = int(input())
def hanoi(n, start, end, temp):
    if n == 0:
        return
    hanoi(n-1, start, temp, end)
    print(start, end)
    hanoi(n-1, temp, end, start)

print(2**n-1)
hanoi(n, 1, 3, 2)