import sys

hour, mi = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
h = n//60
m = n%60

if mi + m >= 60:
    mi = mi+m-60
    hour += 1
else:
    mi += m
hour += h

if hour >= 24:
    hour -= 24

print(hour, mi)