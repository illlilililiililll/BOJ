import sys
from math import factorial
input = sys.stdin.readline

n, r = map(int, input().split())
print(factorial(n)//(factorial(n-r)*factorial(r)))