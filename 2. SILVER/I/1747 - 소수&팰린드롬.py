import sys
input = sys.stdin.readline

n = int(input())
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    else:
        return True

while True:
    if isPrime(n):
        if n == int((str(n)[::-1])):
            print(n)
            break
    n += 1