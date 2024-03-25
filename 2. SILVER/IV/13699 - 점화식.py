import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n+1)]
arr[0] = 1

def t(n):
    if arr[n] != 0:
        return arr[n]
    total = 0
    for i in range(n):
        total += t(i)*t(n-i-1)
    arr[n] = total
    return total

print(t(n))