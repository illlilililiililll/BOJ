import sys

a, b, c = map(int, sys.stdin.readline().split())
n = []
if a==b==c:
    print(10000+a*1000)
elif a==b and a!=c:
    print(1000+a*100)
elif a!=b and b==c:
    print(1000+b*100)
elif a==c and a!=b:
    print(1000+a*100)
elif a!=b!=c:
    n.extend([a, b, c])
    print(max(n)*100)