import sys
from math import factorial
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    total = 0
    for i in range(n+1):
        total += (-1)**i * factorial(n) // factorial(i)
    print(total)