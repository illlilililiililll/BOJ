import sys
input = sys.stdin.readline

n, k = map(int ,input().split())
def fact(n):
    if n == 0:
        return 1
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

print((fact(n)//(fact(n-k)*fact(k)))%10007)