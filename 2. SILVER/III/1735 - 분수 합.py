import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

A, B = map(int, input().split())
C, D = map(int, input().split())
N = gcd(A*D + C*B, B*D) 
print((A*D + C*B)//N, B*D//N)