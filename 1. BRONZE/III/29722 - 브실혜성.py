import sys
input = sys.stdin.readline

y, m, d = map(int, input().split('-'))
f = int(input())

re_y = f//360
re_m = (f-360*re_y)//30
re_d = f-360*re_y-30*re_m

y += re_y
m += re_m
d += re_d
if d > 30:
    m += 1
    d -= 30
if m > 12:
    y += 1
    m -= 12
if m < 10:
    m = '0' + str(m)
if d < 10:
    d = '0' + str(d)

print(y, m, d, sep='-')